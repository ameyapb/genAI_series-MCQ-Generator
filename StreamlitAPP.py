import os
import json
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.logger import logging
from src.mcqgenerator.utils import read_file,get_table_data,wiki_retriever
from src.mcqgenerator.MCQgenerator import generate_evaluate_chain
from langchain.callbacks import get_openai_callback
import streamlit as st
import traceback

with open('/llm/response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

st.title("MCQs Creator App with Langchain!")

with st.form("user_inputs"):
    uploaded_file=st.file_uploader("Upload your PDF or txt file. Incase if you dont have data, leave this field empty")

    mcq_count=st.number_input("No. of MCQ's", min_value=3, max_value=50)

    subject=st.text_input("Insert Subject", max_chars=20)

    tone=st.text_input("Complexity Level of the Questions", max_chars=20, placeholder="Simple")

    button=st.form_submit_button("Create MCQ's")

    if button:
        with st.spinner("loading..."):
            try:
                if uploaded_file is not None:
                    text = read_file(uploaded_file)
                else:
                    text = wiki_retriever(subject)
                with get_openai_callback() as cb:
                    response = generate_evaluate_chain(
                        {
                            "text": text,
                            "number": mcq_count,
                            "subject": subject,
                            "tone": tone,
                            "response_json": json.dumps(RESPONSE_JSON)
                        }
                    )
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")
            
            else:
                print(f"Total Tokens: {cb.total_tokens}")
                print(f"Prompt Tokens: {cb.prompt_tokens}")
                print(f"Completion Tokens: {cb.completion_tokens}")
                print(f"Total Cost: {cb.total_cost}")
                if isinstance(response, dict):
                    quiz=response.get("quiz", None)
                    if quiz is not None:
                        table_data=get_table_data(quiz)
                        if table_data is not None:
                            df=pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)
                            st.text_area(label="Review", value=response["review"])
                        else:
                            st.error("Error in the table data")
                else:
                    st.write(response)