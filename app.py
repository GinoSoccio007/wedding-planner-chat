import streamlit as st
import requests
import json

# Configure the page
st.set_page_config(
    page_title="Wedding Planning Assistant",
    page_icon="💒",
    layout="wide"
)

# Add custom CSS for better styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background-color: #FFF5F5;
    }
    
    /* Chat message styling */
    .chat-message {
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        display: flex;
        align-items: flex-start;
    }
    
    /* User message styling */
    .user-message {
        background-color: #E3F2FD;
        margin-left: 20%;
        margin-right: 5%;
    }
    
    /* Assistant message styling */
    .assistant-message {
        background-color: #FFF0F5;
        margin-right: 20%;
        margin-left: 5%;
    }
    
    /* Icon styling */
    .chat-icon {
        font-size: 24px;
        margin-right: 10px;
    }
    
    /* Header styling */
    h1 {
        color: #FF69B4;
        text-align: center;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Page header
st.title("💒 Wedding Planning Assistant")

# Define message display function
def display_message(message, role):
    icon = "👰" if role == "user" else "💒"
    style_class = "user-message" if role == "user" else "assistant-message"
    
    st.markdown(f"""
        <div class="chat-message {style_class}">
            <div class="chat-icon">{icon}</div>
            <div>{message}</div>
        </div>
    """, unsafe_allow_html=True)

# Display chat history
for message in st.session_state.messages:
    display_message(message["content"], message["role"])

# Chat input
user_input = st.chat_input("Type your message here...")

# Process user input
if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    display_message(user_input, "user")
    
    try:
        # Send request to N8N webhook
        response = requests.post(
            "https://n8n.aiolosmedia.com/webhook/317b952a-f636-4459-9cb4-dbb48613c927",
            json={"message": user_input},
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            # Process assistant response
            assistant_response = response.json().get('content', 'Sorry, I could not process your request.')
            
            # Handle images in response
            def process_images(text):
                import re
                pattern = r'!\[(.*?)\]\((.*?)\)'
                html_image = r'<img src="\2" alt="\1" style="max-width: 100%; height: auto; margin: 10px 0;">'
                return re.sub(pattern, html_image, text)
            
            formatted_response = process_images(assistant_response)
            
            # Add assistant response to history
            st.session_state.messages.append({"role": "assistant", "content": formatted_response})
            display_message(formatted_response, "assistant")
        else:
            st.error(f"Error: Unable to get response (Status code: {response.status_code})")
            
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Add control buttons
st.markdown("---")
cols = st.columns([4,1])
with cols[0]:
    st.markdown("Made with 💝 for your perfect wedding day")
with cols[1]:
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.experimental_rerun()
