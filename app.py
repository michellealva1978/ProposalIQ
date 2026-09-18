import streamlit as st
from pypdf import PdfReader
st.set_page_config(
    page_title="ProposalIQ",
    page_icon="📄",
    layout="wide"
)

st.title("ProposalIQ")
st.subheader("AI RFP / Proposal Analyzer")

st.write(
    "Turn complex RFPs into actionable proposal intelligence."
)

st.info("Upload and AI analysis features are coming next.")
import streamlit as st

st.set_page_config(
    page_title="ProposalIQ | AI RFP Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 ProposalIQ")
st.subheader("AI-Powered RFP & Proposal Analyzer")

st.write(
    """
    ProposalIQ helps proposal teams turn complex RFP documents into
    clear, actionable intelligence — making it easier to identify
    requirements, risks, deadlines, and response priorities.
    """
)

st.divider()

st.markdown("### What ProposalIQ will analyze")

st.write("✓ Key RFP requirements")
st.write("✓ Submission deadlines and deliverables")
st.write("✓ Compliance items")
st.write("✓ Potential risks and red flags")
st.write("✓ Proposal response priorities")

st.info("Portfolio demonstration project created by Michelle Alva")

st.markdown("### Upload an RFP")

uploaded_file = st.file_uploader(
    "Choose an RFP document",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success(f"✓ {uploaded_file.name} uploaded successfully!")
reader = PdfReader(uploaded_file)
    rfp_text = ""

    for page in reader.pages:
        rfp_text += page.extract_text() or ""

    st.write(f"ProposalIQ successfully read {len(reader.pages)} pages.")
