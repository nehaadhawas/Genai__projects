import streamlit as st
import pandas as pd 
import time
from google import genai

def generate_poetry(prompt):
    if prompt:
        msg = st.toast("Finding inspiration...")
        time.sleep(2)
        msg = st.toast("Writing verses...")
        time.sleep(2)
        msg = st.toast("Your poem is ready!", icon="📝")
        time.sleep(2)

        st.write(f"So you want a poem about **{prompt}**.")
        time.sleep(1)
        st.write("Let me craft something beautiful for you... ✨")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Write a short, creative poem about {prompt}"
        )

        st.write(response.text)


if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"   
    client = genai.Client(api_key=API_KEY)

    st.title("✨ Poetry Generator")
    prompt = st.chat_input("What should I write a poem about?")
    generate_poetry(prompt)


