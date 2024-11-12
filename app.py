import streamlit as st
import requests
import time
from datetime import datetime
import json

# Configure page
st.set_page_config(
    page_title="Wedding Planning Assistant",
    page_icon="💒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
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
    .error-message {
        color: #ff4b4b;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .success-message {
        color: #28a745;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'retry_count' not in st.session_state:
    st.session_state.retry_count = 0

# N8N webhook URL
WEBHOOK_URL = "https://n8n.aiolosmedia.com/webhook/317b952a-f636-4459-9cb4-dbb48613c927"

def send_message(message, max_retries=3):
    """Send message to webhook with retry mechanism"""
    for attempt in range(max_retries):
        try:
            response = requests.post(
                WEBHOOK_URL,
                json={"message": message},
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            if response.status_code == 200:
                return response.json()
            else:
                time.sleep(1)  # Wait before retry
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            time.sleep(1)
    return None

# Main content
st.title("💒 Wedding Planning Assistant")
st.markdown("---")

# Quick action buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Find Venues"):
        st.session_state.messages.append({
            "role": "user",
            "content": "I'm looking for wedding venues"
        })
with col2:
    if st.button("Meet Planners"):
        st.session_state.messages.append({
            "role": "user",
            "content": "Show me wedding planners"
        })
with col3:
    if st.button("View Services"):
        st.session_state.messages.append({
            "role": "user",
            "content": "What wedding services do you offer?"
        })

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("Type your wedding planning question here...")

if user_input:
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Show user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Send to webhook with error handling
    try:
        with st.spinner('Getting response...'):
            response = send_message(user_input)
            
        if response:
            with st.chat_message("assistant"):
                st.write(response.get('content', 'I understand your request. Let me help you with that.'))
            st.session_state.messages.append({
                "role": "assistant",
                "content": response.get('content', 'I understand your request. Let me help you with that.')
            })
        else:
            st.error("Unable to get response. Please try again.")
            
    except Exception as e:
        st.error(f"Connection error. Please try again. {str(e)}")
        if st.button("Retry"):
            st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown("*Made with 💝 for your perfect wedding day*")

# Debug information in sidebar
with st.sidebar:
    st.title("Wedding Planner")
    st.markdown("---")
    if st.checkbox("Show Debug Info"):
        st.write("Last Updated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        st.write("Messages in History:", len(st.session_state.messages))
        st.write("Connection Status:", "Connected" if 'response' in locals() else "Not Connected")
