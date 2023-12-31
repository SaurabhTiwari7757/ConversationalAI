import streamlit as st

import os
import google.generativeai as genai

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history = [])
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input = st.text_area("Input:",key = "input")
submit = st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input)
    st.session_stzate['chat_history'].append("You",input)
    st.subheader("The response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append("You",chunk.text)
st.subheader('The chat history is')

for role, text in st.session_state['chat_history']:
    st.write(f'{role}:{text}')
