import sys
import os
import json


import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from business_logic.evaluator import evaluate_business_pairs
from business_logic.data_utils import load_business_profiles


st.set_page_config(page_title="Business Compatibility LLM", layout="wide")
st.title("Business Compatibility LLM")
business_profiles = load_business_profiles()
business_names = [b["name"] for b in business_profiles]

st.markdown("""
**DISCLAIMER:** You may notice inconsistencies or inaccuracies in the AI-generated analysis. Additionally, this tool relies on limited structured data and a language model to generate insights. 
""")


# Input Section
st.header("Business Parties")

selected_a = st.selectbox("Select Business A", business_names, key="biz_a")
selected_b = st.selectbox("Select Business B", business_names, key="biz_b")

biz_a = next((b for b in business_profiles if b["name"] == selected_a), None)
biz_b = next((b for b in business_profiles if b["name"] == selected_b), None)


st.header("Business Attributes")

col1, col2 = st.columns(2)

with col1:
    st.text_input("Business A Name", biz_a["name"], disabled=True, key="biz_a_name")
    st.text_input("Type", biz_a["type"], disabled=True, key="biz_a_type")
    st.text_input("Location", biz_a["location"], disabled=True, key="biz_a_location")
    st.text_input("Capacity", biz_a.get("capacity", "N/A"), disabled=True, key="biz_a_capacity")
    st.text_input("Transport", biz_a.get("transport", "N/A"), disabled=True, key="biz_a_transport")
    st.text_input("Certifications", ", ".join(biz_a.get("certifications", [])), disabled=True, key="biz_a_certifications")

with col2:
    st.text_input("Business B Name", biz_b["name"], disabled=True, key="biz_b_name")
    st.text_input("Type", biz_b["type"], disabled=True, key="biz_b_type")
    st.text_input("Location", biz_b["location"], disabled=True, key="biz_b_location")
    st.text_input("Demand", biz_b.get("demand", "N/A"), disabled=True, key="biz_b_demand")
    st.text_input("Certifications", ", ".join(biz_b.get("certifications", [])), disabled=True, key="biz_b_certifications")


if st.button("Evaluate Compatibility"):
    with st.spinner("Evaluating Compatibility..."):
        result = evaluate_business_pairs(biz_a, biz_b)
        st.success("Analysis Complete")

        st.markdown(result)
