from dotenv import load_dotenv
load_dotenv() # loading all the environment variables from .env file
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get response
model = genai.GenerativeModel("gemini-pro-latest")
def get_response_from_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text

# initializing the streamlit app

st.set_page_config(page_title="Google Gemini Pro LLM", page_icon=":robot_face:")
st.header("Google Gemini Pro LLM :")
input = st.text_input("Enter your question here",key="input")
submit = st.button("Ask the question")
if submit:
    response = get_response_from_gemini(input)
    st.subheader("Response from Google Gemini Pro LLM is:")
    st.write(response)


