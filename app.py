import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("AQ.Ab8RN6J4McrMbr0oAU8WPYBZoFfyB6ZhFxh4TVZHBcRZSutB5g")

client = genai.Client(api_key=api_key)

st.title("🤖 ChatX AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
prompt = st.chat_input("type here...")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    response = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    answer = response.output_text

    with st.chat_message("assistant"):
        st.write(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })