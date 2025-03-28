import streamlit as st
import json

# Title
st.title("📝 AI-Powered Resume Generator")

# Sidebar for User Input
st.sidebar.header("Enter Your Details")

# User Input Fields
name = st.sidebar.text_input("Full Name")
email = st.sidebar.text_input("Email")
phone = st.sidebar.text_input("Phone Number")
linkedin = st.sidebar.text_input("LinkedIn Profile")
skills = st.sidebar.text_area("Skills (comma-separated)")
experience = st.sidebar.text_area("Work Experience (Describe your past roles)")
education = st.sidebar.text_area("Education Details")
projects = st.sidebar.text_area("Projects (Describe key projects you've worked on)")

# Store Data Locally (as JSON)
if st.sidebar.button("Save Details"):
    user_data = {
        "name": name,
        "email": email,
        "phone": phone,
        "linkedin": linkedin,
        "skills": skills.split(","),
        "experience": experience,
        "education": education,
        "projects": projects
    }
    with open("user_data.json", "w") as f:
        json.dump(user_data, f)
    st.sidebar.success("✅ Details Saved Successfully!")

# Load Stored Data
try:
    with open("user_data.json", "r") as f:
        saved_data = json.load(f)
    st.subheader("🔍 Saved Resume Data")
    st.json(saved_data)
except:
    st.info("No user data found. Please enter your details.")
