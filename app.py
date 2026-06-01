import streamlit as st
import requests


st.set_page_config(
    page_title="AI Content Generator",
    layout="wide"
)
st.title("🚀AI Content Generator")
st.write("Generate Blogs,LinkedIN posts,Captions,emails and more")

topic=st.text_input(
    "Enter Topic"
)

technology=st.selectbox(
    "Select Technology",
    [
        "python",
        "React",
        "MERN",
        "NodeJS",
        "FastAPI",
        "AI",
        "GenAI"
    ]
)

content_type=st.selectbox(
    "content type",
    [
        "LinkedIN post",
        "Instagram Captions",
        "Twitter post",
        "Blogs",
        "Email",
        "YouTube Discription"
    ]
)
tone=st.selectbox(
    "Tone",
    [
        "friendly",
        "professional",
        "casual",
        "Technical",
        "Business"
    ]
)
generate=st.button("Generate Content")

if generate:
    
    if topic=="":
        st.warning("please enter topic")
        
    else:
        with st.spinner("Generate Content..."):
            response=requests.post(f"{backend_url}/generate",
            params={
                "topic":topic,
                "technology":technology,
                "content_type":content_type,
                "tone":tone
             }
            )
            st.write("status code:",response.status_code)
            st.write("Response Text:",response.json()["content"])
            st.success("Content Generated Successfully")
            st.subheader("Generated Content")
    