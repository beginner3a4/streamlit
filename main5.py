import streamlit as st
import requests
import pandas as pd

# Streamlit Page Configuration
st.set_page_config(page_title="Talking Database UI", layout="wide")

# Title
st.title("🗂️ Talking Database UI - Ask Questions About Your Data")

# Sidebar
st.sidebar.header("Upload Your Database")
uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

# Initialize Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display Uploaded Data Preview
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.sidebar.write("📊 **Preview of Your Data:**")
    st.sidebar.dataframe(df.head())

# User Input Field
user_input = st.text_input("Ask a question about your data:", key="input", placeholder="Example: 'What is the average price?'")

if st.button("Ask"):
    if user_input and uploaded_file:
        # Convert CSV to JSON for API
        data_json = df.to_json()

        # API Request to FastAPI Backend
        try:
            api_url = "http://127.0.0.1:8000/query"  # Replace with actual FastAPI endpoint
            response = requests.post(api_url, json={"query": user_input, "data": data_json})

            if response.status_code == 200:
                reply = response.json().get("response", "No response received.")
            else:
                reply = "⚠️ Error: Could not fetch a response."

        except requests.exceptions.RequestException:
            reply = "⚠️ Server is not reachable. Check if the FastAPI server is running."

        # Append Messages to Chat History
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.session_state.chat_history.append({"role": "ai", "content": reply})

# Display Chat History
st.write("### Chat History:")
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.markdown(f"👤 **You:** {message['content']}")
    else:
        st.markdown(f"🤖 **AI:** {message['content']}")
