import streamlit as st
import os

# Configure Streamlit
st.set_page_config(
    page_title="Wedding Planner",
    layout="wide"
)

# Your app code
st.title("Wedding Planning Assistant")
st.write("Welcome to your wedding planning journey!")

if st.button("Click me!"):
    st.success("It works!")
