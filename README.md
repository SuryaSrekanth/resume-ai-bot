# 🤖 Personal Resume AI Chatbot

An interactive, AI-powered resume chatbot for your personal portfolio built with **Python**, **Google Gemini API**, and **Streamlit**.

---

## 🌟 Features
- **Grounding with Resume Data**: Answers recruiter questions strictly using a structured `resume_data.json` knowledge base to avoid hallucinated information.
- **Quick Question Chips**: Suggested buttons for top skills, projects, and education.
- **Interactive Chat UI**: Multi-turn chat interface with custom sidebar profile info.
- **Zero Cost Hosting**: Deploys 100% free on Streamlit Community Cloud with Google Gemini's free API tier.

---

## 🚀 Quick Start (Local Setup)

### 1. Project Files Structure
Ensure all files are placed in your project directory:
```text
personal-resume-bot/
├── app.py
├── resume_data.json
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Gemini API Key
1. Get a free API Key from [Google AI Studio](https://aistudio.google.com/).
2. Create a file named `.env` in the project root:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

### 4. Run the Streamlit Application
```bash
streamlit run app.py
```
Open `http://localhost:8501` in your browser.

---

## ☁️ Free Cloud Deployment (Streamlit Community Cloud)

1. **Push to GitHub**:
   Push this project to a new public GitHub repository. *(Ensure `.env` is ignored by `.gitignore`!)*

2. **Deploy on Streamlit**:
   - Go to [share.streamlit.io](https://share.streamlit.io/).
   - Click **New app** and select your GitHub repository.
   - Set Main file path to `app.py`.

3. **Configure Secrets**:
   - Click **Advanced settings** -> **Secrets**.
   - Add:
     ```toml
     GEMINI_API_KEY = "your_actual_api_key_here"
     ```
   - Click **Deploy!**

---

## 📝 Customization
Edit `resume_data.json` with your actual name, contact info, education, skills, and projects to make it your personal AI assistant.
