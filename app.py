import streamlit as st
import time

# Configure page
st.set_page_config(
    page_title="Wedding Planning Assistant",
    page_icon="💒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better loading experience
st.markdown("""
<style>
    .main {
        background-color: #FFF5F5;
    }
    .stButton button {
        background-color: #FF69B4;
        color: white;
        border-radius: 20px;
        padding: 10px 25px;
    }
    div[data-testid="stAppViewContainer"] {
        background-color: #FFF5F5;
    }
</style>
""", unsafe_allow_html=True)

# Main content
st.title("💒 Wedding Planning Assistant")
st.markdown("---")

# Initialize session state
if 'initialized' not in st.session_state:
    with st.spinner('Setting up your wedding planning space...'):
        time.sleep(1)  # Brief pause for loading effect
    st.session_state.initialized = True

# Main interface
if st.session_state.initialized:
    st.write("Welcome to your wedding planning journey! How can I assist you today?")
    
    # Quick action buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Find Venues"):
            st.info("Let's explore perfect venues for your special day!")
    with col2:
        if st.button("Meet Planners"):
            st.info("Discover top wedding planners in your area!")
    with col3:
        if st.button("View Services"):
            st.info("Browse our curated list of wedding services!")

    # Chat interface
    st.markdown("### Start Planning")
    user_input = st.chat_input("Type your wedding planning question here...")
    
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)
        with st.chat_message("assistant"):
            st.write("I'm here to help with your wedding planning needs!")

# Footer
st.markdown("---")
st.markdown("*Made with 💝 for your perfect wedding day*")
