import textwrap

import streamlit as st

st.set_page_config(page_title="Resume Matcher", page_icon="📄")

st.title("📄 Resume Matcher")
st.caption("Compare candidate resumes with role requirements and surface the best-fit profiles instantly.")

st.markdown(
    textwrap.dedent(
        """
        Recruiters waste hours skimming resumes that do not match the expectations of hiring managers. The Resume Matcher agent
        ingests both resumes and job descriptions, normalizes skill entities, and explains every match score in plain language.
        """
    )
)

st.subheader("What you get")
st.markdown(
    """
    - ⚖️ Transparent scoring for skills, experience, and industry alignment.
    - 🔍 Semantic search across resume databases to recommend hidden gems.
    - 📨 Ready-to-send candidate summaries that highlight strengths and risks.
    """
)

st.subheader("Under the hood")
st.markdown(
    """
    1. Chunked embeddings for both resumes and job descriptions with vector stores for retrieval.
    2. Re-ranking using hybrid signals (keyword hits, role seniority, cultural fit prompts).
    3. Feedback loop so recruiters can teach the agent new preferences over time.
    """
)

st.subheader("Usage ideas")
st.markdown(
    """
    - Screen inbound applicants before the hiring manager review meeting.
    - Standardize agency submissions with objective match explanations.
    - Deliver tailored outreach emails that mirror job priorities.
    """
)

if hasattr(st, "page_link"):
    st.page_link("Home.py", label="← Back to portfolio", icon="🏠")
else:
    st.info("Use the Streamlit sidebar to return to the home page.")
