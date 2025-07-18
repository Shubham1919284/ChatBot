import streamlit as st
import streamlit.components.v1 as components
import requests
import json
import time
import os
from datetime import datetime
from io import StringIO

# Page config
st.set_page_config(page_title="DeepSeek Chat", page_icon="🧠", layout="centered")

# Set dark theme by default
if "theme" not in st.session_state:
    st.session_state.theme = "dark"
theme = st.session_state.theme

# Light/Dark Theme CSS
if theme == "dark":
    st.markdown("""
        <style>
        body, .stApp { background-color: #1e1e1e; color: #ffffff; }
        .chat-message { background-color: #2c2c2c; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        body, .stApp { background-color: #f0f2f6; color: #000000; }
        .chat-message { background-color: #ffffff; }
        </style>
    """, unsafe_allow_html=True)

# Theme toggle button
col1, col2 = st.columns([0.85, 0.15])
with col2:
    if st.button("🌙" if theme == "light" else "☀️"):
        st.session_state.theme = "dark" if theme == "light" else "light"
        st.rerun()

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "assistant",
            "content": "Hello! I'm DeepSeek Chat. How can I assist you today?",
            "tokens": None,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    ]

MODEL = "deepseek/deepseek-chat"
temperature = 0.7
max_tokens = 1000

# Load API key from environment variable or fallback
api_key = os.getenv("OPENROUTER_API_KEY", "your_openrouter_api_key_here")

# Display chat messages with avatars, timestamps, and markdown support
for msg in st.session_state.chat_history:
    avatar = "🤖" if msg["role"] == "assistant" else "🧑"
    with st.container():
        st.markdown(f"{avatar} **{msg['role'].capitalize()}** — `{msg['timestamp']}`")
        st.markdown(msg["content"], unsafe_allow_html=True)

# User input
prompt = st.chat_input("Type your message here...")

if prompt:
    st.session_state.chat_history.append({"role": "user", "content": prompt, "tokens": None, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            message_placeholder = st.empty()
            message_placeholder.markdown("...")

            try:
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "HTTP-Referer": "https://deepseek-chat.streamlit.app",
                    "Content-Type": "application/json"
                }
                body = {
                    "model": MODEL,
                    "messages": [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history],
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                    "stream": True
                }
                full_response = ""
                response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body, stream=True)

                for chunk in response.iter_lines():
                    if chunk and chunk.decode('utf-8').startswith("data:"):
                        try:
                            chunk_json = json.loads(chunk.decode('utf-8')[5:])
                            token = chunk_json["choices"][0]["delta"].get("content", "")
                            full_response += token
                            message_placeholder.markdown(full_response)
                        except:
                            continue

                st.session_state.chat_history.append({"role": "assistant", "content": full_response, "tokens": None, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

            except Exception as e:
                error_msg = f"❌ Error: {str(e)}"
                st.session_state.chat_history.append({"role": "assistant", "content": error_msg, "tokens": None, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
                message_placeholder.markdown(error_msg)

# Clear chat button
if st.button("🧹 Clear Current Chat"):
    st.session_state.chat_history = [
        {
            "role": "assistant",
            "content": "Hello! I'm DeepSeek Chat. How can I assist you today?",
            "tokens": None,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    ]
    st.rerun()

# Download chat history
if st.download_button("📥 Download Chat", data=StringIO(json.dumps(st.session_state.chat_history, indent=2)).getvalue(), file_name="chat_history.json", mime="application/json"):
    st.success("✅ Chat history downloaded!")
