# 🏺 KEMET: Voice-to-Booking AI Assistantِ

### *Intelligent Conversational Agent for Smart Egyptian Tourism*

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Cohere](https://img.shields.io/badge/Cohere_AI-Command--R+-082424.svg?style=for-the-badge&logo=cohere&logoColor=white)
![Whisper](https://img.shields.io/badge/OpenAI_Whisper-Transcription-412991.svg?style=for-the-badge&logo=openai&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

---

## 📖 Overview

**KEMET** (كيميت) is a sophisticated **Voice-First AI Agent** designed to modernize the tourism experience in Egypt. Built with **Cohere's Command-R+** and **OpenAI's Whisper**, the system acts as a digital concierge that understands natural voice commands to recommend hotels, provide historical context, and automate the entire booking process from voice to email voucher.

### 🎙️ The Voice-First Revolution
Unlike traditional booking apps, Kemet focuses on **Natural Human Interaction**:
* **Zero-UI Dependency**: Users can complete a full booking cycle just by speaking.
* **Context-Aware Reasoning**: The system doesn't just search; it "reasons" why a specific hotel fits the user's spoken request.

---


https://github.com/user-attachments/assets/5c834379-122d-44b3-a391-b7d4e99be08e


## 🏗️ Project Structure

```bash
kemet/                       # Root Directory
├── 📂 venv/                   # Virtual Environment
├── 🐍 app.py                  # Main Streamlit UI & Session Management
├── 🐍 logic.py                # Core AI Pipeline (Whisper & LLM Logic)
├── 📄 hotels.json             # Structured Database of Egyptian Tourism
├── 📄 .env                    # Secret Configuration (API Keys & SMTP)
├── 📄 .gitignore              # Git Exclusion Rules
├── 📄 README.md               # Professional Documentation
└── 📦 requirements.txt        # Project Dependencies Manifest

```

---

## 🧠 Advanced AI Pipeline

The system ensures a seamless user journey through a multi-stage intelligent workflow:

1. **Acoustic Processing**: Utilizes `OpenAI Whisper (Base)` to transcribe live microphone input into high-quality text, handling diverse accents and background noise.
2. **Intent & Entity Extraction**: Employs `Cohere's Command-R` to parse the user's speech and extract key entities like **Location**, **Hotel Category**, and **Preferences**.
3. **Reasoned Recommendation**: The LLM analyzes the `hotels.json` database and provides a "Best Match" with a logical explanation of why this hotel was chosen.
4. **Automated Transactional Agent**: Once a choice is made, an autonomous agent generates a unique **Confirmation Code** and prepares the booking metadata.
5. **Secure SMTP Voucher Delivery**: A dedicated mailing module handles secure `SMTP_SSL` communication to send a professional PDF-like voucher to the user's email.

---

## ✨ Core Highlights

* **🏆 Smart Ranking**: Automatically filters and ranks hotels in Cairo, Giza, and other major spots based on real-time user intent.
* **🛡️ Session Integrity**: Uses `Streamlit Session State` to maintain booking data across the workflow, ensuring no information is lost between recording and emailing.
* **📧 End-to-End Automation**: Integrated with Gmail's secure app-passwords to deliver instant ticket vouchers.
* **🌍 Scalable Database**: The system is designed to handle thousands of hotel entries via its structured JSON-based storage.

---

## 🛠️ Technical Stack

| Component | Technology | Role |
| --- | --- | --- |
| **Frontend** | `Streamlit` | Interactive Web UI |
| **Speech-to-Text** | `OpenAI Whisper` | Voice Transcription |
| **Reasoning Engine** | `Cohere (Command-R+)` | Intent Analysis & Logic |
| **Audio Handler** | `Pydub / Audio-Recorder` | Real-time Voice Capture |
| **Mailing** | `SMTPLib (SSL)` | Voucher Delivery System |

---

## 🚀 Setup & Deployment

### 1️⃣ Installation

```bash
git clone https://github.com/minasamy01/Kemet-AI-Voice-tourism-Assistant.git
cd Kemet-AI-Voice-tourism-Assistant
pip install -r requirements.txt

```

### 2️⃣ Configuration (Create `.env`)

```env
COHERE_API_KEY=your_cohere_key_here
EMAIL_SENDER = xxxxxxx@gmail.com
EMAIL_PASSWORD=your_app_password_here

```

### 3️⃣ Launch

```bash
streamlit run app.py

```


---

## 🛠️ Future Roadmap: The Evolution of KEMET

We are moving towards a more robust, **Agentic Architecture** to transform KEMET into a truly autonomous travel companion. Upcoming updates include:

### 1️⃣ Advanced RAG Pipeline (Retrieval-Augmented Generation)

* **Knowledge Base Expansion**: Transitioning from a static JSON to a **Vector Database (FAISS/ChromaDB)** to index thousands of historical documents, travel guides, and real-time hotel availability.
* **Semantic Search**: Implementing **LangChain’s Multi-Query Retriever** to understand nuanced tourist queries even when they don't match exact keywords.

### 2️⃣ Agentic Framework with LangChain

* **Tool Use & Function Calling**: Moving from hard-coded logic to **LangChain Agents**. The LLM will have "Tools" to check live weather, convert currencies, or query the Google Maps API autonomously.
* **Memory Management**: Integrating `ConversationSummaryBufferMemory` to allow the AI to remember user preferences across different sessions for a personalized experience.

### 3️⃣ Multi-Modal monument Recognition

* **Vision Integration**: Utilizing **Gemini 1.5 Pro/Flash** to allow users to upload photos of monuments and receive instant historical narrations via voice.

### 4️⃣ Real-time Data Sync

* **Live API Integration**: Replacing the mock booking logic with real-time API fetches for actual hotel prices and flight availability.

---


## 👨‍💻 Author

# **Mina Samy**
### *AI & NLP Engineer*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mina-data-ai/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BaJL%2F1WTcT2eyQjurm1ZczQ%3D%3D) 
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/minasamy01)

---

