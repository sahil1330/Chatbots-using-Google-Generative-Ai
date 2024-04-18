# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai
import subprocess
from IPython.display import display
from IPython.display import Markdown


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response =chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Chat")
def run_image_ai():
    subprocess.run(["streamlit", "run", "vision.py"])

def run_invoice_ai():
    subprocess.run(["streamlit", "run", "invoice.py"])

# with st.container():
#     with st.columns([1, 2, 1]):
#         st.write(image_ai)
#         st.write(invoice_ai)
cols = st.columns([1, 2])
with cols[0]:
    image_ai = st.button("Image Ai")
    if image_ai:
        run_image_ai()
with cols[1]:
    invoice_ai = st.button("Invoice Ai")
    if invoice_ai:
        run_invoice_ai()

st.header("Gemini Application")

input=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")


## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    for chunk in response:
        print(st.write(chunk.text))
        print("_"*80)
    
    st.write(chat.history)