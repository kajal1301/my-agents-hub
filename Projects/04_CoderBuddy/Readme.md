# 🧑‍💻 CoderBuddy

Agentic AI project builder inspired by **Lovable** — built with  
**Streamlit + LangGraph + LangChain + Groq (openai/gpt-oss-120b)**.

---

## Features
- Verifies if a prompt is engineering/app-building.
- Asks clarifying questions with LangChain memory.
- Planner → Architect → Coder multi-agent graph.
- Generates a runnable web app and downloadable ZIP.

---

## Directory
coderbuddy/
├─ app.py # Streamlit UI
├─ requirements.txt
├─ .env.example # environment variable template
├─ .gitignore
├─ README.md
└─ agents/
├─ init.py
├─ model_client.py # Groq API client
├─ state.py # Graph state definitions
├─ nodes.py # Verifier / Planner / Architect / Coder nodes
├─ graph.py # LangGraph graph definition
└─ file_writer.py # write & zip generated project

yaml
Copy code

---

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add GROQ_API_KEY
streamlit run app.py