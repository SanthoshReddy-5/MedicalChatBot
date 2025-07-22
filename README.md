## 🩺 First Aid Bot – **Retrieval-Augmented Generation (RAG)** application
A responsive web-based **Medical Chatbot** designed to provide medical information. It uses **Google Gemini API**, **Pinecone**, **Sentence Transformers**, **Flask** and the knowledge base is powered by context from **The Gale Encyclopedia of Medicine (Second Edition)**.

## 📸 Screenshots
<img width="1915" height="902" alt="image" src="https://github.com/user-attachments/assets/bcdc8bb1-7325-4565-8f58-946aaf43f0d7" />

## 🚀 Features
- 🩺 RAG pipeline for medical Q&A
- 📖 Contextual responses from The Gale Encyclopedia of Medicine
- 🔍 Semantic vector search using SentenceTransformers
- ⚡ Fast retrieval via Pinecone
- 🧠 Response generation via Google Gemini API
- 🌐 Clean UI with Flask, HTML, CSS, JS
- 🕓 Chat interface with timestamps

## 📚 Source of Medical Knowledge
- The Gale Encyclopedia of Medicine (Second Edition)
- Used under fair use for educational and research purposes.

## 🛠️ Tech Stack

| Purpose                | Technology                     |
|------------------------|--------------------------------|
| Embedding              | SentenceTransformers           |
| Vector DB              | Pinecone                       |
| Language Model         | Google Gemini API              |
| Backend Framework      | Flask                          |
| Frontend               | HTML, CSS, JS (Responsive UI)  |

## 📁 Project Structure
```
MedicalChatBot/
├── app.py # Main Flask application
├── upload_pdf.py # Script to upload data into Pinecone
├── create_pinecone_index.py # Script for creating Pinecone index
├── templates/ # HTML templates
│ ├── index.html
│ └── about.html
├── static/ # Static assets
│ ├── style.css
│ ├── script.js
│ ├── logo.png
│ └── developer.jpg
├── data/ # Embedded or uploaded data (PDF's)
| └── medical_book.pdf
├── .env # Environment variables (ignored)
├── .gitignore # Git ignore rules
├── requirements.txt # Python dependencies
└── README.md # You're reading it!
```

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/SanthoshReddy-5/MedicalChatBot.git
cd MedicalChatBot
```

### 2. Set up a Virtual Environment (optional)
```bash
python -m venv venv
venv\Scripts\activate  # On MacOs: source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env file and Set Environment Variables
```bash
PINECONE_API_KEY=your_pinecone_api_key
GEMINI_API_KEY=your_gemini_api_key
```

### 5. Create Pinecone Index and Upload the Data
Run the following command to create your Pinecone index
```bash
python create_pinecone_index.py
```
Once your Pinecone index is created, run the following command to process and upload your PDF data
```bash
python upload_pdf.py
```
Once the index is created and your data is uploaded, you can start the flask web app using the following command
```bash
python app.py
```
🚀 This will launch the Flask development server, Go to http://127.0.0.1:5000 in your browser.
