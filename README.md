# 🤖 AskBuddy - AI QnA Chatbot

A simple, Streamlit-powered Q&A chatbot built with **LangChain** and **Google Gemini** (Gemini 2.5 Flash). AskBuddy runs a chat interface in your browser and streams answers from Google's Gemini model.

## ✨ Features

- 💬 Interactive chat UI built with Streamlit
- 🧠 Powered by Google Gemini via LangChain (`gemini-2.5-flash`)
- 💾 Conversation history kept per session (via `st.session_state`)
- 🔑 API key managed through a `.env` file

## 🛠 Tech Stack

- **Python 3.14**
- [Streamlit](https://streamlit.io) - web UI
- [LangChain](https://python.langchain.com) - LLM integration (`langchain-google-genai`)
- [Google Gemini](https://ai.google.dev/) - LLM backend
- [uv](https://docs.astral.sh/uv/) - package & environment manager

## 📁 Project Structure

```
.
├── src/qa_chatbot/       # package module (entry point defined in pyproject.toml)
├── main.py               # Streamlit app entry point
├── pyproject.toml        # project config & dependencies
├── uv.lock               # locked dependency versions
├── .env                  # secret config (GOOGLE_API_KEY)
└── .python-version       # python version pin (3.14)
```

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) installed
- A Google AI API key (from [Google AI Studio](https://aistudio.google.com/))

### 2. Install dependencies

```bash
uv sync
```

### 3. Set up your API key

Create a `.env` file in the project root with your Google API key:

```env
GOOGLE_API_KEY=your-google-api-key-here
```

> ⚠️ Never commit your `.env` file. Add it to `.gitignore` to keep your API key secure.

### 4. Run the app

```bash
streamlit run main.py
```

Or via the package script:

```bash
uv run qa-chatbot
```

Your browser will open at `http://localhost:8501`. Start asking questions!

## 🧪 Usage

1. Open the app in your browser
2. Type a question into the input box at the bottom ("Ask anything?")
3. AskBuddy replies with an answer from Gemini
4. Conversation history persists for the duration of the session

## 📝 Notes

- The default model is `gemini-2.5-flash` — you can change it in `main.py` (`llm = ChatGoogleGenerativeAI(...)`).
- A CLI loop is included (commented out) in `main.py` as an alternative way to interact with the model.