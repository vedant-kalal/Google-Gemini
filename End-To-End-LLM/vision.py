import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro-latest")
def get_response_from_gemini(img, prompt):
    response = model.generate_content([prompt,img])
    return response.text
    
st.set_page_config(page_title="Google Gemini Pro Vision LLM", page_icon=":robot_face:")
st.header("Google Gemini Pro Vision LLM :")
input = st.file_uploader("Upload your image here", type=["png", "jpg", "jpeg"])
prompt = st.text_input("Enter your question here",key="prompt") 

if input is not None:
    img = Image.open(input)
    st.image(img, caption='Uploaded Image.', use_column_width=True)
else:
    img = None

submit = st.button("tell me about the image")

if submit:
    if img is not None and prompt:
        response  = get_response_from_gemini(img, prompt)
        st.subheader("Response from Google Gemini Pro Vision LLM is:")
        st.write(response)
    elif img is None:
        st.subheader("Please upload an image.")
    else:
        st.subheader("Please enter a prompt.")