import streamlit as st
from data_handling import get_text_or_df
from agentic_analysis import generate_response_from_text, generate_response_from_df
import pandas as pd

st.title("Data Analyst Agent")

file = st.file_uploader("Upload any file", type=["csv", "xlsx", "txt", "pdf", "docx", "png", "jpg", "jpeg"])
if file:
    filetype = file.name.split(".")[-1]
    content = get_text_or_df(file, filetype)

    st.success(f"File `{file.name}` uploaded successfully!")

    question = st.text_input("Ask a question about the file:")
    if question:
        with st.spinner("Analyzing..."):
            if isinstance(content, pd.DataFrame):
                st.dataframe(content.head())
                answer = generate_response_from_df(content, question)
            else:
                st.text_area("Extracted text", content[:2000])
                answer = generate_response_from_text(content, question)
            st.markdown("Answer:")
            st.write(answer)
