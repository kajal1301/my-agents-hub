# 🧑‍💻 CoderBuddy

Agentic AI app builder inspired by Lovable. It takes your idea, asks clarifying questions, plans the architecture, and generates a runnable project you can download as a ZIP — all inside a Streamlit UI.

Built with Streamlit, LangGraph, LangChain, and Groq (model: `openai/gpt-oss-120b`).

---

## Features
- Prompt verification to ensure it’s an engineering/app-building task
- Clarifying questions with short-term conversation memory
- Multi-agent flow: Verifier → Requirements → Planner → Architect
- Generates code artifacts and offers a one-click ZIP download
- Preview section (renders README or HTML when available)

---

## Requirements
- Python 3.9+
- A Groq API key (for model access)

---

## Setup
```bash
# from the project root
cd Projects/04_CoderBuddy

# (optional but recommended) create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate

# install dependencies
pip install -r requirements.txt

# set your environment (create .env if needed)
# GROQ_API_KEY=your_key_here
```

---

## Run
```bash
streamlit run app.py
```

Open the Local URL shown in the terminal (usually http://localhost:8501).

---

## Usage
1. Enter your app idea in the prompt box.
2. Click “Run CoderBuddy 🚀”.
3. Answer any clarifying questions and click Run again.
4. When code artifacts are generated, use “Download Project ZIP 📦” to save the project.

Notes:
- The app hides raw code in the UI and shows a Preview if a README or HTML page is available.
- The ZIP contains all generated files so you can run or iterate locally.

---

## Project structure
```
Projects/04_CoderBuddy/
├─ app.py                # Streamlit UI
├─ requirements.txt
├─ pyproject.toml
├─ .gitignore
├─ Readme.md
└─ agents/
   ├─ __init__.py
   ├─ filewriter.py      # write & zip generated project
   ├─ graph.py           # LangGraph graph definition
   ├─ model.py           # LLM client setup
   ├─ nodes.py           # Verifier / Requirements / Planner / Architect
   └─ state.py           # Graph state definitions
```

---

## Environment variables
Create a `.env` file next to `app.py` with:
```
GROQ_API_KEY=your_key_here
```

---

## Troubleshooting
- If you see missing packages, run `pip install -r requirements.txt` again.
- If the port is busy, Streamlit will start on a different port (e.g., 8502).
- On macOS, for better file-change reloads, install Watchdog:
  ```bash
  xcode-select --install
  pip install watchdog
  ```
- If you changed dependencies, restart Streamlit after reinstalling packages.

---

## License
MIT