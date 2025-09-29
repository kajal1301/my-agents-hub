from typing import List, Dict
from .model import groq_client, MODEL_NAME
from .state import GraphState, PlanSchema, ArchitectureSchema, FileCode
import json

SYSTEM_BASE = """You are CoderBuddy, an agentic software engineer.
Follow software engineering best practices (specs, SOLID, tests, docs).
Always return STRICT JSON when asked for JSON. No backticks."""

def _chat(messages, temperature=0.2):
    client = groq_client()
    resp = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=temperature,
        messages=messages,
    )
    return resp.choices[0].message

# 1) Verifier Node: is it engineering/app-building?
def verifier_node(state: GraphState) -> GraphState:
    user = state["user_prompt"]
    sys = SYSTEM_BASE + """
Task: Classify if the user request is about building a software project/web/app/tool or other engineering work.
Answer 'true' or 'false' JSON: {"is_engineering": true|false, "reason": "..."}"""
    msg = _chat([
        {"role":"system", "content": sys},
        {"role":"user", "content": user}
    ])
    data = {"is_engineering": False}
    try:
        data = json.loads(msg.content)
    except Exception:
        pass
    state["is_engineering"] = bool(data.get("is_engineering", False))
    state["status"] = ("Verified: engineering" if state["is_engineering"] 
                       else "Not engineering; ask for engineering prompt")
    return state

# 2) Requirement Gatherer Node: ask clarifying questions
def requirements_node(state: GraphState) -> GraphState:
    if not state.get("is_engineering"):
        # Propose how to reframe
        state["questions"] = [
            "Please describe the app you want me to build (purpose, users).",
            "What platform do you prefer (web, mobile, desktop)?",
            "Any tech stack preferences (React, Next.js, FastAPI, Streamlit, Postgres, etc.)?",
            "List the must-have features and any nice-to-haves.",
        ]
        return state

    sys = SYSTEM_BASE + """
Task: From the user's initial prompt, generate up to 6 clarifying questions to fully specify requirements (scope, data, users, features, constraints, integration).
Return JSON: {"questions": [ "...", ... ]}"""
    msg = _chat([
        {"role":"system", "content": sys},
        {"role":"user", "content": state["user_prompt"]}
    ])
    try:
        data = json.loads(msg.content)
        state["questions"] = data.get("questions", [])
    except Exception:
        state["questions"] = []
    return state

# 3) Planner Node
def planner_node(state: GraphState) -> GraphState:
    sys = SYSTEM_BASE + """
You are the Planner. Create a project plan:
- name, description
- suggested tech_stack (be pragmatic)
- features (prioritized)
- files to create with path and purpose (follow standard project layout)
Target: small/medium web apps; prefer simplicity.

Return JSON matching:
{
 "project_name": "...",
 "description": "...",
 "tech_stack": ["..."],
 "features": ["..."],
 "files": [{"path":"...", "purpose":"..."}, ...]
}"""
    questions = state.get("questions", [])
    answers = state.get("answers", {})
    prompt = {
        "original_prompt": state["user_prompt"],
        "qa": [{"q": q, "a": answers.get(q, "")} for q in questions]
    }
    msg = _chat([
        {"role":"system", "content": sys},
        {"role":"user", "content": json.dumps(prompt)}
    ])
    plan = {}
    try:
        plan = json.loads(msg.content)
        PlanSchema(**plan)  # validate
    except Exception:
        plan = {
            "project_name":"fallback_app",
            "description":"Auto-generated app",
            "tech_stack":["python","streamlit"],
            "features":["home page"],
            "files":[{"path":"README.md","purpose":"overview"}]
        }
    state["plan"] = plan
    state["files"] = plan.get("files", [])
    state["status"] = "Planned"
    return state

# 4) Architect Node
def architect_node(state: GraphState) -> GraphState:
    sys = SYSTEM_BASE + """
You are the Architect. Based on the plan, produce:
- a concise architecture description
- UML-like diagram (ASCII ok)
- components (name, responsibility, depends_on)
- minimal data_models (name, fields)
- build & run instructions (for dev)

Return JSON matching:
{
 "diagram_uml":"...",
 "components":[{"name":"...", "responsibility":"...", "depends_on":["..."]}],
 "data_models":[{"name":"...", "fields":[{"name":"...", "type":"..."}]}],
 "build_run_instructions": "..."
}"""
    msg = _chat([
        {"role":"system", "content": sys},
        {"role":"user", "content": json.dumps(state.get("plan", {}))}
    ])
    arch = {}
    try:
        arch = json.loads(msg.content)
        ArchitectureSchema(**arch)  # validate
    except Exception:
        arch = {
            "diagram_uml":"[App] -> [Backend]\n[Backend] -> [DB]",
            "components":[{"name":"UI","responsibility":"input/output","depends_on":["Backend"]}],
            "data_models":[],
            "build_run_instructions":"pip install -r requirements.txt; streamlit run app.py"
        }
    state["architecture"] = arch
    state["status"] = "Architected"
    return state

# 5) Coder Node
def coder_node(state: GraphState) -> GraphState:
    sys = SYSTEM_BASE + """
You are the Coder. Generate concrete file contents for EACH file in plan.files.
Rules:
- Provide production-ready, runnable code.
- For Python+Streamlit, ensure `streamlit run app.py` works.
- Include README with setup instructions.
- Include requirements if needed.
Return STRICT JSON: {"artifacts":[{"path":"...", "content":"..."}]}
"""
    payload = {
        "plan": state.get("plan", {}),
        "architecture": state.get("architecture", {}),
        "files": state.get("files", []),
    }
    # Ask for code
    msg = _chat([
        {"role":"system", "content": sys},
        {"role":"user", "content": json.dumps(payload)}
    ], temperature=0.1)
    artifacts = []
    try:
        data = json.loads(msg.content)
        artifacts = data.get("artifacts", [])
        # validation
        _ = [FileCode(**a) for a in artifacts]
    except Exception:
        # fallback minimal app
        artifacts = [
            {"path":"app_package/__init__.py","content":""},
            {"path":"app.py","content":"""import streamlit as st
st.set_page_config(page_title="CoderBuddy App")
st.title("Hello from CoderBuddy")
st.write("This is a minimal generated app.")"""},
            {"path":"README.md","content":"# Generated app\\nRun: `pip install -r requirements.txt && streamlit run app.py`"},
            {"path":"requirements.txt","content":"streamlit>=1.37\\n"},
        ]
    state["code_artifacts"] = artifacts
    state["status"] = "Code generated"
    return state
