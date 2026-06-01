import streamlit as st
import requests

backend_url = st.secrets["backend_url"]

st.title("AI Content Generator")

topic = st.text_input("Topic")
technology = st.text_input("Technology")

content_type = st.selectbox(
    "Content Type",
    ["Blog", "Article", "LinkedIn Post"]
)

tone = st.selectbox(
    "Tone",
    ["Professional", "Casual", "Technical"]
)

if st.button("Generate Content"):

    try:
        response = requests.post(
            f"{backend_url}/generate",
            params={
                "topic": topic,
                "technology": technology,
                "content_type": content_type,
                "tone": tone
            },
            timeout=60
        )

        st.write("Status Code:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            st.success("Content Generated Successfully")
            st.subheader("Generated Content")
            st.write(data["content"])

        else:
            st.error(f"Backend Error: {response.status_code}")
            st.code(response.text)

    except Exception as e:
        st.error(str(e))