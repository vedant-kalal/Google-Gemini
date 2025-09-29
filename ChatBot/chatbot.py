from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-pro")

## function to load Gemini Pro model and get response
chat = model.start_chat(history=[])

def get_gemini_response(prompt):
    response = chat.send_message(prompt,stream=True) # stream=True means, it will return the response in chunks
    return response

# initializing the streamlit app
st.set_page_config(page_title="Google Gemini Pro LLM Chatbot", page_icon=":robot_face:")
st.header("Google Gemini Pro LLM Chatbot :")

# initializing the session state to store the chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Enter your message here:",key="input")

submit = st.button("Send")
if submit and input:
    response = get_gemini_response(input)
    # add user message and bot response to the chat history
    st.session_state['chat_history'].append(("you", input))
    st.subheader("Response from Google Gemini Pro LLM is:")
    for chunk in response:
        st.write(chunk.text, end='', flush=True)
        st.session_state['chat_history'].append(("bot", chunk.text))

st.subheader("Chat History:")
for role,text in st.session_state['chat_history']:
    if role == "you":
        st.markdown(f"**You:** {text}")
        st.markdown("**Bot:** ", unsafe_allow_html=True)
    else:
        st.markdown(text)