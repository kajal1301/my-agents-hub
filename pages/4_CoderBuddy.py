import textwrap

import streamlit as st

st.set_page_config(page_title="CoderBuddy", page_icon="🤝")

st.title("🤝 CoderBuddy")
st.caption("Plan, scaffold, and review application features with an agentic development partner.")

st.markdown(
    textwrap.dedent(
        """
        CoderBuddy orchestrates a graph of specialised tools that collaborate to turn product prompts into production-ready
        projects. From clarifying requirements to packaging a downloadable ZIP, the agent keeps builders in the loop at every
        stage.
        """
    )
)

st.subheader("Agent workflow")
st.markdown(
    """
    1. **Understand** – Ask targeted clarifying questions and verify the request is an engineering task.
    2. **Plan** – Draft multi-step implementation plans with architecture outlines and component breakdowns.
    3. **Build** – Generate code artifacts, preview READMEs/HTML, and bundle everything for download.
    4. **Iterate** – Maintain short-term memory so your follow-up feedback refines the same project.
    """
)

st.subheader("Interface tour")
st.markdown(
    """
    - 📥 Prompt panel to describe the app you want.
    - 🧠 Conversation memory viewer that surfaces the dialogue history.
    - 📦 One-click project export with a downloadable ZIP archive.
    """
)

st.subheader("Powering technology")
st.markdown(
    """
    - LangChain graph agents for branching workflows.
    - Groq-hosted `openai/gpt-oss-120b` for fast instruction following.
    - Streamlit UI with persistent session state and memory controls.
    """
)

if hasattr(st, "page_link"):
    st.page_link("Home.py", label="← Back to portfolio", icon="🏠")
else:
    st.info("Use the Streamlit sidebar to return to the home page.")
