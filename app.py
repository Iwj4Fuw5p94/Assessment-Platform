# app.py
import streamlit as st
from azure_openai import generate_response
from langchain_integration import ask_question
 
# Streamlit Interface
st.title('Hexaware AI Assessment Platform')
 
# Recruiter: Upload Custom Questions
uploaded_file = st.file_uploader("Upload your questions", type=["txt", "pdf"])
 
if uploaded_file is not None:
    question = uploaded_file.getvalue().decode("utf-8")
    st.text_area("Question:", value=question, height=200)
 
# Candidate: Answer the question
user_input = st.text_input("Enter your response here")
 
if user_input:
    response = ask_question(user_input)  # Use Langchain or Azure OpenAI
    st.write(f"AI Response: {response}")