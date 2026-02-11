import textwrap

import streamlit as st

st.set_page_config(page_title="Text-to-SQL Analyst", page_icon="🗄️")

st.title("🗄️ Text-to-SQL Analyst")
st.caption("Ask business questions in natural language and receive executable SQL with context-aware safeguards.")

st.markdown(
    textwrap.dedent(
        """
        This agent wraps a semantic layer around your warehouse so analysts and stakeholders can explore data without
        memorizing table names. It reasons over metadata, samples schemas, and produces human-readable summaries together
        with the SQL it generates.
        """
    )
)

st.subheader("Highlights")
st.markdown(
    """
    - 💬 Conversational follow-ups that refine filters, time ranges, or aggregations.
    - 🔒 Guardrails that validate SQL against allowed tables, row limits, and query cost.
    - 📝 Automatic insight summaries so insights can be pasted directly into reports.
    """
)

st.subheader("Workflow")
st.markdown(
    """
    1. Connect to Snowflake, BigQuery, or Postgres with read-only credentials.
    2. Sync schema descriptions and business metrics from your catalog.
    3. Chat with the agent; execute SQL safely with one click once you approve the plan.
    """
)

st.subheader("Extensibility")
st.markdown(
    """
    - Plug in domain-specific validators (PII leakage checks, SLA thresholds, etc.).
    - Cache embeddings so popular questions return instantly.
    - Stream results into Streamlit visualisations or external BI tools.
    """
)

if hasattr(st, "page_link"):
    st.page_link("Home.py", label="← Back to portfolio", icon="🏠")
else:
    st.info("Use the Streamlit sidebar to return to the home page.")
