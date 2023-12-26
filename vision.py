from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input,image):
    if input !="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini LLM Image")
st.header("Gemini LLM Image")
input=st.text_input("Input: ", key="input")

file_upload = st.file_uploader("Choose an image..", type=["jpg","jpeg", "png"])
image=""
if file_upload is not None:
    image=Image.open(file_upload)
    st.image(image, caption="Image Uploaded", use_column_width=True)

submit=st.button("Describe about the image")

if submit:
    response=get_gemini_response(input,image)
    st.subheader('The response is ...')
    st.write(response)
