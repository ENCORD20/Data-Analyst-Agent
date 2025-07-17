import pandas as pd
from together_client import query_llama_maverick

def generate_response_from_text(text: str, user_question: str) -> str:
    prompt = f"""You are a data analyst. Based on the following document content:
{text[:2000]}  # Only first 2,000 chars to avoid token limit
Answer this: {user_question}
"""
    return query_llama_maverick(prompt)

def generate_response_from_df(df: pd.DataFrame, user_question: str) -> str:
    sample_data = df.head(10).to_markdown()
    prompt = f"""You are a data analyst. Here's a sample of the dataset:

{sample_data}

Answer the following question about the data: {user_question}
"""  
    return query_llama_maverick(prompt)

