📄 RAG PDF Viewer

A simple Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions based on their content.

Built using:

LangChain
Streamlit
Hugging Face
🚀 Features
📂 Upload PDF files
✂️ Automatic text chunking
🔍 Semantic search using embeddings
🤖 Context-aware question answering
⚡ Simple and interactive UI
🧠 How it works

This project implements a RAG pipeline, which combines:

Retrieval → finding relevant chunks from the document
Generation → answering using an LLM

This approach improves accuracy by grounding responses in actual document content instead of pure generation

📁 Project Structure
rag-pdf-viewer/
│── app.py              # Streamlit UI
│── utils.py            # Core RAG logic
│── requirements.txt    # Dependencies
│── .env                # API keys (not pushed)
│── .gitignore
⚙️ Installation
1. Clone the repository
git clone https://github.com/Garvit-562/RAG-PDF-viewer.git
cd RAG-PDF-viewer
2. Create virtual environment
python -m venv venv

Activate:

venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
4. Add Hugging Face API key

Create a .env file:

HUGGINGFACEHUB_API_TOKEN=your_token_here
5. Run the app
streamlit run app.py
🖥️ Usage
Upload a PDF file
Wait for processing
Ask questions in natural language
Get answers based on document content
🔧 Tech Stack
Frontend: Streamlit
Backend: Python
LLM: Hugging Face models
Embeddings: Sentence Transformers
Vector Store: FAISS
⚠️ Limitations
May produce incorrect answers if context retrieval fails
Performance depends on chunking and embeddings
Free-tier APIs may be slow or rate-limited
🔥 Future Improvements
✅ Chat history / memory
✅ Source citations (very important for RAG)
✅ Multi-document support
✅ Better models (Mistral / LLaMA)
✅ Persistent vector database
