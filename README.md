🌟 LangGraph + Gemini Chatbot Simulator (Streamlit Edition)
<p align="center"> <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" /> <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit" /> <img src="https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-4285F4?logo=google" /> <img src="https://img.shields.io/badge/LangChain-Framework-orange?logo=chainlink" /> <img src="https://img.shields.io/badge/LangGraph-Orchestration-green" /> </p> <p align="center"> <b>Multi-turn conversational AI powered by LangGraph + Gemini, delivered in a clean Streamlit web app.</b> </p>
🚀 Overview

This project demonstrates how to build a stateful, multi-turn AI chatbot using:

LangGraph for workflow orchestration

Google Gemini 2.5 Flash via LangChain

Streamlit for an elegant, real-time chat interface

The chatbot follows a controlled conversation loop:

Ask a question

Send question to Gemini

Ask user if they want to continue

Loop based on “yes/no”

This makes it a perfect example for AI workflows, LLM routing, Graph-based state machines, and interactive UI development.

✨ Features
🔁 LangGraph Conversation Flow

Implements a full conversation pipeline:

ask_question → chatbot → ask_another_question → (yes → repeat / no → end)

💬 Streamlit Chat UI

Powered by:

st.chat_message()

st.chat_input()

session state for continuity

⚡ Gemini 2.5 Flash Integration

Ultra-fast text generation via:

ChatGoogleGenerativeAI(model="gemini-2.5-flash")

🧠 Stateful Multi-Turn Dialogue

Conversation history preserved across turns.

🔧 Easy to Extend

Add memory, analytics, database logging, buttons, or additional graph nodes.

🛠️ Tech Stack
Component	Description
LangGraph	LLM workflow graph and router
LangChain	LLM wrappers + message objects
Gemini (Google Generative AI)	Fast reasoning model
Streamlit	Beautiful web UI
Python dotenv	Secure API key loading
📁 Project Structure
├── app.py                # Streamlit web app
├── requirements.txt      # Dependencies
├── .env                  # API key (ignored by GitHub)
└── README.md             # Project documentation (this file)

🔧 Setup & Installation
1️⃣ Clone the repository
git clone https://github.com/Jasman123/AI_Chat.git


2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add your Gemini API Key

Create a .env file:

GOOGLE_API_KEY=your_key_here

▶️ Run the Application

Start the Streamlit app:

streamlit run app.py


Streamlit will launch at:

http://localhost:8501

📸 Screenshot (Optional)

Add your screenshot or GIF here
(Streamlit chat UI looks great with a dark theme!)

🌱 Future Enhancements

 Add chat memory

 Add vector database (Pinecone, Chroma, etc.)

 Add multiple LLM models

 Add “chat history download” button

 Deploy via Docker

 Deploy to Streamlit Cloud

🤝 Contributing

Contributions are welcome!
Feel free to submit issues, ideas, and pull requests.

⭐ Support the Project

If you like this project, consider giving it a ⭐ on GitHub — it helps more people discover it!

🧑‍💻 Author
