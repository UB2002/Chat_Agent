import streamlit as st
from back import analyze_data  # Import directly from server.py

st.title("Titanic Dataset Chat Agent")

question = st.text_input("Ask a question about the Titanic dataset:")

if question:
    try:
        text_answer, viz_bytes = analyze_data(question)
        st.write("**Answer:**", text_answer)
        if viz_bytes:
            st.image(viz_bytes, caption="Generated Visualization")
    except Exception as e:
        st.error(f"Error processing your request: {str(e)}")