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

def show_responsive_preview(html: str, height: int = 600):
    # Renders an iframe that expands to its container; the HTML runs inside
    container_css = """
    <style>
      .cb-frame { width: 100%; max-width: 1280px; margin: 8px auto 0; }
      .cb-toolbar { display:flex; gap:8px; margin: 6px 0 8px; flex-wrap: wrap; }
      .cb-toolbar button { padding:6px 10px; border:1px solid #e5e7eb; background:#fff; border-radius:8px; cursor:pointer; }
      .cb-iframe-wrap { width:100%; border:1px solid #e5e7eb; border-radius:12px; overflow:hidden; }
      .cb-iframe { width:100%; height: %dpx; border:0; }
    </style>
    """ % height
    toolbar = """
    <div class="cb-toolbar">
      <button onclick="parent.postMessage({type:'cb-size',w:375,h:667},'*')">iPhone (375×667)</button>
      <button onclick="parent.postMessage({type:'cb-size',w:768,h:1024},'*')">iPad (768×1024)</button>
      <button onclick="parent.postMessage({type:'cb-size',w:1024,h:768},'*')">Laptop (1024×768)</button>
      <button onclick="parent.postMessage({type:'cb-size',w:'100%',h:%d},'*')">Auto</button>
    </div>
    """ % height
    wrapper = f"""
      <div class="cb-frame">
        {toolbar}
        <div id="wrap" class="cb-iframe-wrap">
          <iframe id="cb_iframe" class="cb-iframe"></iframe>
        </div>
      </div>
      <script>
        const html = `{html.replace('`','\\`')}`;
        const ifr = document.getElementById('cb_iframe');
        const blob = new Blob([html], {{ type: 'text/html' }});
        const url = URL.createObjectURL(blob);
        ifr.src = url;

        window.addEventListener('message', (e)=>{
            if(!e.data || e.data.type !== 'cb-size') return;
            const w = e.data.w, h = e.data.h;
            const wrap = document.getElementById('wrap');
            if (typeof w === 'string') wrap.style.width = w; else wrap.style.width = w + 'px';
            if (typeof h === 'string') ifr.style.height = h; else ifr.style.height = h + 'px';
        });
      </script>
    """
    components.html(container_css + wrapper, height=height + 90, scrolling=False)


from agents.graph import build_graph
from agents.state import GraphState
from agents.filewriter import write_project, memory_safe_get
from agents.preview import build_inlined_preview_html
import streamlit.components.v1 as components

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
# ZIP generation (unchanged)
colA, colB = st.columns([1,1])
with colB:
    if st.button("Generate Project ZIP 📦", type="secondary"):
        artifacts = (last or {}).get("code_artifacts") or []
        if not artifacts:
            # fallback: minimal files if model produced none
            artifacts = [
                {"path":"index.html","content":"<!doctype html><html><head><meta charset='utf-8'><title>Preview</title></head><body><h2>Empty project</h2></body></html>"}
            ]
        zip_path = write_project(artifacts, base_dir="generated_project")
        with open(zip_path, "rb") as f:
            st.download_button("⬇️ Download ZIP", f, file_name="coderbuddy_project.zip", mime="application/zip")


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
    # Plan / Architecture preview
    if last.get("plan") or last.get("architecture"):
        st.subheader("3️⃣ Live Preview")
        artifacts = (last or {}).get("code_artifacts") or []
        html = build_inlined_preview_html(artifacts)
        show_responsive_preview(html, height=640)

    # if last.get("plan"):
    #     st.subheader("3️⃣ Plan")
    #     st.json(last["plan"])

    if last.get("architecture"):
        st.subheader("4️⃣ Architecture")
        st.json(last["architecture"])

    if last.get("code_artifacts"):
        st.subheader("5️⃣ Preview")
        artifacts = last["code_artifacts"]
        # Try to render a helpful preview if possible
        readme = next((a for a in artifacts if a.get("path"," ").lower().endswith("readme.md")), None)
        html_page = next((a for a in artifacts if a.get("path"," ").lower().endswith(".html")), None)
        if readme:
            st.markdown(readme["content"])
        elif html_page:
            st.components.v1.html(html_page["content"], height=650, scrolling=True)
        else:
            st.success("Project generated. Download the ZIP to view the full app.")

        with st.expander("Files included"):
            for a in artifacts[:50]:
                st.markdown(f"- **{a['path']}**")

        zip_path = write_project(artifacts, base_dir="generated_project")
        with open(zip_path, "rb") as f:
            st.download_button(
                "Download Project ZIP 📦",
                f,
                file_name="coderbuddy_project.zip",
                mime="application/zip",
            )

st.divider()
st.subheader("Conversation Memory")
for m in st.session_state.memory.load_memory_variables({}).get("history", []):
    st.markdown(f"- **{m.type.capitalize()}**: {m.content}")
