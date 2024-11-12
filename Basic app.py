import streamlit as st
import time

# Give the server a moment to start
time.sleep(5)

# Simple app
st.title("Test App")
st.write("Basic test page")

# Health status
st.sidebar.write("Server Status: Active")
