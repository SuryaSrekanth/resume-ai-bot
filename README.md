# 🤖 Personal AI Resume Bot

An interactive, AI-driven portfolio assistant designed to let recruiters, hiring managers, and visitors chat directly with an AI persona trained on my professional background, skills, projects, and work history.

---

## 🌟 Overview

The **Personal AI Resume Bot** transforms traditional static PDFs and portfolio websites into a dynamic conversational experience. Instead of scanning through long documents, visitors can ask specific questions like:
- *"What experience do you have with React, Node.js, and Cloud architectures?"*
- *"Can you tell me about a project where you solved a difficult technical challenge?"*
- *"Are you available for full-time or contract roles?"*

The bot responds in real time with accurate, contextual insights backed by my verified project and work history.

---

## ✨ Key Features

- 💬 **Interactive Conversational Q&A**: Ask natural language questions about my resume, past roles, and engineering background.
- 🎯 **Role & Skill Matching**: Instant responses detailing relevant project experience aligned with specific job descriptions or skill requirements.
- 📚 **RAG-Powered Knowledge Base**: Leverages Retrieval-Augmented Generation (RAG) to source answers directly from factual career data.
- 🎨 **Modern & Responsive Interface**: Styled with sleek dark mode aesthetics, glassmorphism, and smooth micro-animations.
- ⚡ **Fast & Lightweight**: Built for low-latency responses and seamless web embedding on portfolio sites.
- 🔒 **Guardrails & Privacy**: Structured system prompts ensure responses stay professional, accurate, and aligned with career goals.

---

## 🛠️ Architecture & Tech Stack

```
┌───────────────────┐      ┌─────────────────────┐      ┌─────────────────────────┐
│   User / Visitor  │ ───► │  Frontend Web UI    │ ───► │   API / Serverless      │
└───────────────────┘      └─────────────────────┘      └─────────────────────────┘
                                                                     │
                                                                     ▼
                                                        ┌─────────────────────────┐
                                                        │ LLM + RAG Engine        │
                                                        │ (Resume Knowledge Base) │
                                                        └─────────────────────────┘
```

- **Frontend**: HTML5, Modern CSS / Tailwind, JavaScript (React / Vite)
- **AI / LLM Integration**: OpenAI / Gemini API / LangChain
- **Knowledge Base**: Structured JSON / Markdown Resume Context
- **Deployment**: Vercel / GitHub Pages / Cloudflare Workers

---

## 🚀 Planned Roadmap

- [x] Initial Repository & Documentation Setup
- [ ] **Phase 1**: Structure Resume & Project Knowledge Base (JSON / Vector Store)
- [ ] **Phase 2**: Develop API endpoints and LLM integration with RAG context
- [ ] **Phase 3**: Build modern, responsive Chat Interface UI
- [ ] **Phase 4**: Add suggested prompt chips (e.g., *"Top Skills"*, *"Featured Projects"*)
- [ ] **Phase 5**: Deploy live demo to Portfolio website

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.
