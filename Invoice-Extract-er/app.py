from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image
import google.generativeai as genai


load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_respone(input, image, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input, image[0], prompt])
    return response.text


def input_image_setup(uploaded_file):

    if uploaded_file is not None:
        #Read file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type" : uploaded_file.type,
                "data" : bytes_data            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Found!!")
    
st.set_page_config(page_title="Invoice Extractor")
st.header("Gemini Application")

input = st.text_input("Input Prompt: ", key="input")
upload_file = st.file_uploader("Choose an Image... ", type= ["jpg", "jpeg", "png"])
image =  ""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded Image", use_container_width= True)
submit = st.button("Tell me about the invoice")

input_prompt = """
You are an expert in understanding in invoices.
you will receive input image and invoices and you will have to 
have to answer question based on that input image 
"""

if  submit:
    image_data = input_image_setup(upload_file)
    response = get_gemini_respone(input_prompt, image_data, input)

    st.subheader("The Response is")
    st.write(response)

