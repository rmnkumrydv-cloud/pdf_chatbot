📄 PDF Chatbot

Interact with your PDF documents using natural language — ask questions and get accurate answers instantly.

🚀 Hosted Live: https://pdf-chatbot-grok.streamlit.app/

🔥 Features

📚 Upload multiple PDF files

🤖 Chat with your documents using natural language

🧠 High-quality responses powered by language models

⚡ Fast retrieval with vector search (FAISS + embeddings)

🗣️ Streaming answer responses like ChatGPT

🧵 Conversation memory — history persists

💬 Clean chat-style UI

🛠️ How It Works

Upload PDFs: Select one or more PDF documents

Process Text: The app reads PDFs and splits them into chunks

Vector Embeddings: Text is converted into vectors using MiniLM

Vector Search: FAISS retrieves relevant chunks

LLM Interaction: Ask questions and get real-time streamed responses

🧪 Try It Out

Just visit the deployed app and upload your PDFs — then start asking questions!

👉 https://pdf-chatbot-grok.streamlit.app/

📥 Supported Documents

✔ Standard text-based PDFs
❌ Scanned image-only PDFs (no built-in OCR)

📌 Usage

Open site

Upload PDF files in the sidebar

Click Process

Ask your question using chat input

Chat history persists

Example prompts:

“What are the main points in this document?”

“Summarize section two.”

“Who are the key people mentioned?”

💻 Code & Deployment

This project uses:

Technology	Purpose
Streamlit	UI
Groq LLaMA-3	LLM / answer generation
FAISS	Vector search
MiniLM	Text embeddings
pypdf	PDF text extraction
LangChain	LLM chaining & memory
Python	Backend
📂 Installation
git clone https://github.com/rmnkumrydv-cloud/pdf_chatbot.git
cd pdf_chatbot
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
streamlit run app.py
🔐 Environment Vars

Create a .env:

GROQ_API_KEY=your_groq_key_here

(This key enables the LLM backend.)

🧠 UI / Features Screenshot

<img width="1869" height="946" alt="image" src="https://github.com/user-attachments/assets/cc2868c9-48b5-413c-9d62-a2b152cc998e" />


⚙ Deployment

Deployed using Streamlit Cloud
Branch: main
Main file: app.py

Add secret GROQ_API_KEY in Streamlit Cloud settings.

🤝 Credits

Built by rmnkumrydv-cloud
Powered by Streamlit, LangChain, Groq, FAISS, and MiniLM

📜 License

MIT License (or license of your choice)
