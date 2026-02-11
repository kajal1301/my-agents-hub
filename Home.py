import textwrap

import streamlit as st

st.set_page_config(
    page_title="My Agents Hub Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Hi, I'm An AI Solutions Builder 👋")
st.caption(
    "I craft practical LLM agents, retrieval pipelines, and data apps that automate workflows and delight users."
)

with st.container():
    left, right = st.columns([2, 1])
    with left:
        st.subheader("About Me")
        st.markdown(
            textwrap.dedent(
                """
                - 🔭 **Current Focus:** Designing agentic systems that mix reasoning with reliable tool use.
                - 🧠 **Core Strengths:** Python, LangChain, RAG pipelines, prompt engineering, and UX-friendly Streamlit apps.
                - 🤝 **Collaboration Style:** Fast prototyping, clear communication, and data-informed iteration.
                """
            )
        )
    with right:
        st.subheader("Let's Connect")
        st.markdown(
            """
            - 📧 **Email:** [you@example.com](mailto:you@example.com)
            - 💼 **LinkedIn:** [linkedin.com/in/your-profile](https://www.linkedin.com/in/your-profile/)
            - 🧾 **Resume:** [View PDF](https://example.com/resume.pdf)
            """
        )

st.divider()

st.header("Featured Projects")
st.markdown(
    "Explore the four flagship agents that anchor this hub. Each card links to a dedicated page with goals, features, and usage notes."
)

projects = [
    {
        "title": "Invoice Auditor",
        "emoji": "🧾",
        "description": "Autonomous quality checks for vendor invoices with discrepancy detection and approval workflows.",
        "focus": "Finance automation • Document QA • Agents",
        "page": "pages/1_Invoice_Auditor.py",
    },
    {
        "title": "Text-to-SQL Analyst",
        "emoji": "🗄️",
        "description": "Conversational data analysis that turns natural language into executable SQL over governed datasets.",
        "focus": "Analytics copilots • Retrieval • SQL synthesis",
        "page": "pages/2_Text_to_SQL.py",
    },
    {
        "title": "Resume Matcher",
        "emoji": "📄",
        "description": "RAG-powered talent screener that compares resumes with job descriptions for instant fit scoring.",
        "focus": "HR tech • Retrieval • Evaluation",
        "page": "pages/3_Resume_Matcher.py",
    },
    {
        "title": "CoderBuddy",
        "emoji": "🤝",
        "description": "Agentic development assistant that plans, codes, and reviews app features with iterative memory.",
        "focus": "Dev tools • Planning • Memory",
        "page": "pages/4_CoderBuddy.py",
    },
]

for i in range(0, len(projects), 2):
    cols = st.columns(2, gap="large")
    for col, project in zip(cols, projects[i : i + 2]):
        with col:
            st.subheader(f"{project['emoji']} {project['title']}")
            st.markdown(project["description"])
            st.caption(project["focus"])
            if hasattr(st, "page_link"):
                st.page_link(project["page"], label="Open project page ➜")
            else:
                if st.button(
                    f"Open {project['title']}",
                    key=f"open_{project['title'].lower().replace(' ', '_')}",
                ):
                    try:
                        st.switch_page(project["page"])
                    except Exception:
                        st.info(
                            "Navigation is available from the Streamlit sidebar if buttons are disabled."
                        )

st.divider()

st.header("How I Work")
st.markdown(
    textwrap.dedent(
        """
        1. **Discover** the real workflow pain point and map the target success metric.
        2. **Prototype** rapidly in Streamlit, wiring LLM reasoning with robust tool calling.
        3. **Evaluate** with guardrails, human feedback, and telemetry before deployment.
        """
    )
)

st.success(
    "Need a bespoke agent or data workflow? Drop me a note and let's build something users love."
)
