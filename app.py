import streamlit as st

st.set_page_config(page_title="Wedding Planner", layout="wide")

st.title("Wedding Planning Assistant")
st.write("Welcome to your wedding planning journey!")

if st.button("Click me!"):
    st.success("It works!")
