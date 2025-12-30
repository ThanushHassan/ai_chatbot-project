import streamlit as st

with open("college_faq.txt", "r") as file:
    data = file.read()

st.write(data)


