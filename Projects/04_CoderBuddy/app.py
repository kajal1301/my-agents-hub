import streamlit as st
from dotenv import load_dotenv
load_dotenv()

# LangChain memory with fallback if import fails
try:
    from langchain.memory import ConversationBufferWindowMemory
except Exception:
    class ConversationBufferWindowMemory:
        def __init__(self, k=8, return_messages=True):
            self.k, self.return_messages = k, return_messages
            self._hist = []
        def save_context(self, human, ai):
            self._hist.append(("human", human.get("human","")))
            self._hist.append(("ai", ai.get("ai","")))
            self._hist = self._hist[-2*self.k:]
        def load_memory_variables(self, _):
            return {"history": [type("M", (), {"type": t, "content": c}) for t,c in self._hist]}
        def clear(self): self._hist.clear()

from agents.graph import build_graph
from agents.state import GraphState
from agents.filewriter import write_project, memory_safe_get

st.set_page_config(page_title="CoderBuddy", layout="wide")
st.title("🧑‍💻 CoderBuddy — Agentic App Builder")

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferWindowMemory(k=8, return_messages=True)
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "graph" not in st.session_state:
    st.session_state.graph = build_graph()
if "last_state" not in st.session_state:
    st.session_state.last_state = {}

with st.sidebar:
    st.header("⚙️ Settings")
    st.caption("Using Groq's `openai/gpt-oss-120b` model.")
    if st.button("Clear Memory"):
        st.session_state.memory.clear()
        st.session_state.answers = {}
        st.session_state.last_state = {}
        st.success("Memory cleared.")

st.subheader("1️⃣ Describe the app you want to build")
user_prompt = st.text_area("Your prompt", height=140)

colA, colB = st.columns([1,1])
with colA:
    run_btn = st.button("Run CoderBuddy 🚀")
with colB:
    gen_btn = st.button("Generate Project ZIP 📦", disabled=True)

if run_btn and user_prompt.strip():
    st.session_state.memory.save_context({"human": user_prompt}, {"ai": "Processing..."})
    initial_state: GraphState = {
        "user_prompt": user_prompt.strip(),
        "answers": st.session_state.answers
    }
    final_state = st.session_state.graph.invoke(initial_state)
    st.session_state.last_state = final_state

last = st.session_state.last_state
if last:
    st.info(f"Status: {last.get('status','')}")
    if not last.get("is_engineering", False):
        st.warning("This doesn't look like an engineering prompt.")

    qs = memory_safe_get(last, "questions", [])
    if qs:
        st.subheader("2️⃣ Clarifying questions")
        with st.form("answers_form"):
            new_answers = {}
            for q in qs:
                new_answers[q] = st.text_area(q, height=80)
            submitted = st.form_submit_button("Save Answers")
            if submitted:
                st.session_state.answers.update({k:v for k,v in new_answers.items() if v})
                st.success("Answers saved. Click Run again to refine.")

    if last.get("plan"):
        st.subheader("3️⃣ Plan")
        st.json(last["plan"])

    if last.get("architecture"):
        st.subheader("4️⃣ Architecture")
        st.json(last["architecture"])

    if last.get("code_artifacts"):
        st.subheader("5️⃣ Generated files")
        for a in last["code_artifacts"][:12]:
            st.markdown(f"**{a['path']}**")
            st.code(a["content"][:2000], language="markdown")
        st.session_state["zip_ready"] = True
        gen_btn = st.button("Generate Project ZIP 📦", type="secondary")

    if gen_btn and last.get("code_artifacts"):
        zip_path = write_project(last["code_artifacts"], base_dir="generated_project")
        with open(zip_path, "rb") as f:
            st.download_button("Download ZIP", f, file_name="coderbuddy_project.zip", mime="application/zip")

st.divider()
st.subheader("Conversation Memory")
for m in st.session_state.memory.load_memory_variables({}).get("history", []):
    st.markdown(f"- **{m.type.capitalize()}**: {m.content}")
