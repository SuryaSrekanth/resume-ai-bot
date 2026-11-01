import os
import json
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load local environment variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="Chat with My AI Resume",
    page_icon="🤖",
    layout="centered"
)

# Fetch API Key safely without triggering StreamlitSecretNotFoundError when running locally
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    try:
        if "GEMINI_API_KEY" in st.secrets:
            api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

if not api_key:
    st.error("⚠️ Gemini API Key not found! Please set GEMINI_API_KEY in your .env file or Streamlit Secrets.")
    st.info("💡 Get your free API Key from Google AI Studio: https://aistudio.google.com/")
    st.stop()

# Initialize Gemini Client
client = genai.Client(api_key=api_key)

# Load Resume Data
@st.cache_data
def load_resume_data():
    with open("resume_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

resume_data = load_resume_data()

# System Instructions to Ground the AI Model
system_instruction = f"""
You are an AI Assistant representing {resume_data.get('name')}. Your goal is to answer recruiters, hiring managers, and portfolio visitors accurately, professionally, and warmly.

Guidelines:
1. Base all your answers ONLY on the following Resume Knowledge Base:
{json.dumps(resume_data, indent=2)}

2. Answer in first-person ("I") or as a helpful career assistant ("{resume_data.get('name')} is experienced in...").
3. Keep responses concise, structured, clear, and engaging.
4. If a user asks something NOT covered in the resume, politely explain that it isn't listed, and invite them to reach out via email ({resume_data['contact']['email']}).
"""

# Sidebar Profile Info
with st.sidebar:
    if os.path.exists("profile.jpg"):
        st.image("profile.jpg", use_container_width=True)
    elif os.path.exists("profile.png"):
        st.image("profile.png", use_container_width=True)
    st.title(f"👤 {resume_data.get('name')}")
    st.caption(f"🚀 {resume_data.get('headline')}")
    st.markdown("---")
    st.subheader("📫 Contact Details")
    st.markdown(f"- 📧 **Email**: [{resume_data['contact']['email']}](mailto:{resume_data['contact']['email']})")
    st.markdown(f"- 💼 **LinkedIn**: [Profile]({resume_data['contact']['linkedin']})")
    st.markdown(f"- 🐙 **GitHub**: [Profile]({resume_data['contact']['github']})")
    st.markdown(f"- 📍 **Location**: {resume_data['contact']['location']}")
    
    st.markdown("---")
    st.subheader("💡 About Me")
    st.write(resume_data.get('summary'))
    
    st.markdown("---")
    st.caption("Built with Python, Google Gemini API & Streamlit")

# Main Title & Greeting
st.title("🤖 Chat with My Portfolio AI")
st.write(f"Welcome! Ask me anything about **{resume_data.get('name')}**'s skills, projects, education, or experience.")

# Quick Prompt Suggestions
st.markdown("**Suggested Questions:**")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🛠️ Top Skills"):
        st.session_state["user_input"] = "What are your top technical skills?"
with col2:
    if st.button("🚀 Projects"):
        st.session_state["user_input"] = "Tell me about your top projects."
with col3:
    if st.button("🎓 Education"):
        st.session_state["user_input"] = "What is your educational background?"

# Initialize Chat History in Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": f"Hi! I'm the AI assistant for {resume_data.get('name')}. What would you like to know today?"}
    ]

# Display Existing Chat Messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Process Input (either from chat input or quick prompt button)
prompt = st.chat_input("Ask a question about my resume...")
if "user_input" in st.session_state and st.session_state["user_input"]:
    prompt = st.session_state.pop("user_input")

if prompt:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Format history for Gemini call
    formatted_contents = []
    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "model"
        formatted_contents.append(types.Content(role=role, parts=[types.Part.from_text(text=msg["content"])]))

    # Generate response from Gemini
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            bot_reply = None
            last_error = None
            
            # Try available models in order of preference
            for model_name in ["gemini-2.5-flash-lite"]:
                try:
                    response = client.models.generate_content(
                        model=model_name,
                        contents=formatted_contents,
                        config=types.GenerateContentConfig(
                            system_instruction=system_instruction,
                            temperature=0.3
                        )
                    )
                    if response and response.text:
                        bot_reply = response.text
                        break
                except Exception as e:
                    last_error = str(e)
                    continue

            if bot_reply:
                st.markdown(bot_reply)
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            else:
                st.error("⚠️ Could not generate a response from Gemini API.")
                if "RESOURCE_EXHAUSTED" in str(last_error) or "Quota exceeded" in str(last_error):
                    st.warning("⏳ **Quota / Rate Limit Exceeded**: Your API key has hit its free-tier rate limit. Please wait 1 minute or generate a fresh API key at [Google AI Studio](https://aistudio.google.com/).")
                elif "API_KEY_INVALID" in str(last_error) or "400" in str(last_error):
                    st.warning("🔑 **Invalid API Key**: Please verify your API key in `.env` from [Google AI Studio](https://aistudio.google.com/).")
                else:
                    st.info(f"Details: {last_error}")
