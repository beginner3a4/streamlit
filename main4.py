import streamlit as st
import requests

# Streamlit Page Configuration
st.set_page_config(page_title="Health Coach Chatbot")

# Title and Sidebar
st.title("OUR NEW PROJECT 🚀")


# Initialize Chat History in Session State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User Input Field
user_input = st.text_input("Ask me anything about health:", key="input", placeholder="Type here...")

if st.button("Send"):
    if user_input:
        # Append User Query to Chat History
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Send request to FastAPI chatbot
        response = requests.post("fastApi", json={"query": user_input})
        if response.status_code == 200:
            reply = response.json()["response"]
        else:
            reply = "Sorry, something went wrong. Please try again."

        # Append AI Response to Chat History
        st.session_state.chat_history.append({"role": "ai", "content": reply})

# Display Chat History
st.write("### Chat History:")
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.markdown(f"👤 **You:** {message['content']}")
    else:
        st.markdown(f"🤖 **AI:** {message['content']}")

