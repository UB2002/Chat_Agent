import streamlit as st
import requests

st.title("Titanic Dataset Chat Agent")

question = st.text_input("Ask a question about the Titanic dataset:")

if question:
    response = requests.post("http://127.0.0.1:8000/analyze", json={"question": question})
    if response.status_code == 200:
        result = response.json()
        st.write("**Answer:**", result["text"])
        if result["visualization"]:
            st.image(result["visualization"], caption="Generated Visualization")
    else:
        st.error("Error processing your request.")