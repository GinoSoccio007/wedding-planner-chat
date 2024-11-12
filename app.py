import streamlit as st
import os

# Your existing Streamlit app code here

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8501))
    st.run(port=port)
