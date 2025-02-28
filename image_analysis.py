import streamlit as st
import google.generativeai as genai
from PIL import Image

## provide you api key###

api_key = "AIzaSyDNXDFxH9tKiEwv5LlSNb5Rdjp79tiw7Jw"
genai.configure(api_key=api_key)

## choose th heading #######
st.header("Image analytics")

### upload file ###
upload_file = st.file_uploader("Upload and image", type=["png","jpg","jpeg"])

if upload_file is not None:
    st.image(Image.open (upload_file))


####### what you want to ask####
prompt = st.text_input("Enter the text")

### use genai model###

if st.button("GET RESPONSE"):
    img = Image.open(upload_file)
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content([prompt, img])
    st.markdown(response.text)
