from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image
load_dotenv() # loading all the environment variables from .env file
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-pro")

## function to load Gemini Pro model and get response
def get_gemini_response(input,image,prompt):# input is , how user wants to make the ai act like, means the role of ai, like "You are a helpful assistant","you are a python expert"
    model_input = [input]
    if image:
        model_input.append(image[0])
    if prompt:
        model_input.append(prompt)
    
    response = model.generate_content(model_input, stream=True) # stream=True means, it will return the response in chunks
    response.resolve()
    return response.text

def input_image_setup(uploaded_image):
    if uploaded_image is not None:
        bytes_data = uploaded_image.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_image.type, # get the mime type of the image
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise ValueError("No image uploaded")
    
# initializing the streamlit app
st.set_page_config(page_title="MultiLanguage Invoice Extractor", page_icon=":robot_face:")
st.header("MultiLanguage Invoice Extractor :")
image = st.file_uploader("Upload your invoice image here", type=["png", "jpg", "jpeg"])

img = ""
if image is not None:
    img = Image.open(image)
    st.image(img, caption='Uploaded Image.', use_container_width=True)

input = st.text_input("Enter the operation you want to perform:",key="input")

submit = st.button("Extract Invoice Data")
input_prompt = ''' 
you are an invoice data extraction expert. i will upload an invoice image and you will have to answer any questions based on uploaded invoice image.
'''
# if submit button is clicked, then get the response from the model
if submit:
    # read file and convert it to bytes
    image_data = input_image_setup(image)
    response = get_gemini_response(input_prompt,image_data,input)
    st.subheader("The extracted data from the invoice is:")
    st.write(response)
