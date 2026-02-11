import textwrap

import streamlit as st

st.set_page_config(page_title="Invoice Auditor", page_icon="🧾")

st.title("🧾 Invoice Auditor")
st.caption("Autonomous quality checks for vendor invoices with discrepancy detection and approvals.")

st.markdown(
    textwrap.dedent(
        """
        The Invoice Auditor agent reviews uploaded invoices, extracts structured fields, and flags compliance issues before
        payments are released. It is ideal for finance teams that want to automate tedious checks without losing traceability.
        """
    )
)

st.subheader("Why it matters")
st.markdown(
    """
    - ✅ Catch duplicate or inflated charges automatically before they hit the ledger.
    - 🧠 Maintain a conversation log so reviewers understand every recommendation the agent makes.
    - 📊 Export clean JSON/CSV audit trails for downstream ERP or analytics systems.
    """
)

st.subheader("Key features")
st.markdown(
    """
    1. OCR and layout parsing that normalize invoices from different suppliers.
    2. Policy checks for tax IDs, contract alignment, and anomaly detection.
    3. Approval routing with summarized findings for human controllers.
    """
)

st.subheader("Try it out")
st.markdown(
    """
    1. Upload a batch of sample invoices (PDF or image).
    2. Provide business rules (tolerances, valid vendors, currency conversions).
    3. Receive a scored report plus suggested remediation steps.
    """
)

if hasattr(st, "page_link"):
    st.page_link("Home.py", label="← Back to portfolio", icon="🏠")
else:
    st.info("Use the Streamlit sidebar to return to the home page.")
