# 🤖 GenAI Week 1

This repository contains my Week 1 GenAI learning projects. The goal is to understand how Large Language Models (LLMs) work by making API calls and building a simple terminal chatbot.

---

## 📂 Project Structure

```
Gen-AI/
│
├── API_call1.py         # First API call using Google Gemini API
├── chatbot.py           # CLI chatbot with conversation history
├── requirements.txt     # Project dependencies
├── .gitignore           # Files ignored by Git
├── .env                 # API key (not included in GitHub)
└── README.md
```

---

## 🚀 Features

### Project 1: First API Call
- Connects to the Google Gemini API
- Sends a prompt
- Receives and prints the AI response

### Project 2: Terminal Chatbot
- Command Line Interface (CLI)
- Multi-turn conversation
- Maintains chat history
- Exit command to end the chat

---

## 🛠️ Technologies Used

- Python 3.11
- Google Gemini API
- python-dotenv

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
```

### 2. Navigate to the project

```bash
cd Gen-AI
```

### 3. Create a virtual environment

```bash
python3.11 -m venv venv
```

### 4. Activate the virtual environment

**macOS/Linux**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```


---

## ▶️ Run the Projects

### First API Call

```bash
python API_call1.py
```

### Terminal Chatbot

```bash
python chatbot.py
```

Type your message and start chatting.

To exit:

```text
exit
```

---



