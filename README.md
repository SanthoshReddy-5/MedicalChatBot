# 🩺 First Aid Bot – **Retrieval-Augmented Generation (RAG)** application

A responsive web-based **Medical Chatbot** designed to provide first-aid and medical information. It uses **Google Gemini API**, **Pinecone**, **Sentence Transformers**, **Flask** and the knowledge base is powered by context from **The Gale Encyclopedia of Medicine (Second Edition)**.

---

## 🚀 Features

- 🩺 RAG pipeline for medical Q&A
- 📖 Contextual responses from The Gale Encyclopedia of Medicine
- 🔍 Semantic vector search using SentenceTransformers
- ⚡ Fast retrieval via Pinecone
- 🧠 Response generation via Google Gemini API
- 🌐 Clean UI with Flask, HTML, CSS, JS
- 🕓 Chat interface with timestamps

---

## 🧩 How RAG Works Here

User Query --> Embed (Sentence Transformer)
--> Search Pinecone Index (Top-k Chunks)
--> Send Chunks + User Query to Gemini
--> Gemini Generates Final Answer

---

## 🛠️ Tech Stack

| Purpose                | Technology                     |
|------------------------|--------------------------------|
| Embedding              | SentenceTransformers           |
| Vector DB              | Pinecone                       |
| Language Model         | Google Gemini API              |
| Backend Framework      | Flask                          |
| Frontend               | HTML, CSS, JS (Responsive UI)  |

---

## 📁 Project Structure

├── app.py # Main Flask application
├── upload_pdf.py # Script to upload and embed Gale Encyclopedia PDF
├── templates/ # HTML templates
│ ├── index.html
│ └── about.html
├── static/ # Static assets
│ ├── style.css
│ ├── script.js
│ ├── logo.png
│ └── developer.jpg
├── data/ # Embedded or uploaded data (PDFs, vectors)
├── .env # Environment variables (ignored)
├── .gitignore # Git ignore rules
├── requirements.txt # Python dependencies
└── README.md # You're reading it!


---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/medical-chatbot.git
cd medical-chatbot

Set up a Virtual Environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

 Install Dependencies
pip install -r requirements.txt

Set Environment Variables

Create a .env file:

env
Copy
Edit
FLASK_APP=app.py
FLASK_ENV=development
PINECONE_API_KEY=your_pinecone_key
PINECONE_ENV=your_pinecone_environment
GEMINI_API_KEY=your_gemini_api_key

. Upload and Index the Medical Book
Ensure upload_pdf.py is configured with the correct PDF path and run:

bash
Copy
Edit
python upload_pdf.py

Run the Application
bash
Copy
Edit
flask run
Go to http://127.0.0.1:5000 in your browser.
📸 Screenshots
(Add your app screenshots here — showing the chatbot interface, about page, etc.)

📚 Source of Medical Knowledge
Gale Encyclopedia of Medicine (Second Edition)
Used under fair use for educational and research purposes.
