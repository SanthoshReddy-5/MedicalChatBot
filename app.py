from flask import Flask, render_template, request,jsonify
from pinecone import Pinecone
from google.generativeai import configure, GenerativeModel
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Configure your keys
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PINECONE_INDEX_NAME="medicalbot"

# Configure Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX_NAME)

# Configure Gemini
configure(api_key=GEMINI_API_KEY)
gemini_model = GenerativeModel("gemini-2.0-flash")

# Free Embeddings (Sentence-Transformers)
embedding_model = SentenceTransformer("multi-qa-MiniLM-L6-cos-v1")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/getAnswer", methods=["POST"])
def get_bot_response():
    user_query = request.json["message"]

    # Embed query
    query_embedding = embedding_model.encode(user_query).tolist()

    # Query Pinecone
    query_response = index.query(
        vector=query_embedding,
        top_k=5,
        include_metadata=True
    )

    chunks = []
    for match in query_response["matches"]:
        if "metadata" in match and "text" in match["metadata"]:
            chunks.append(match["metadata"]["text"])

    context_text = "\n\n".join(chunks)

    # Build prompt
    prompt = (
        f"You are an expert assistant. Use the following context from the PDF to answer the question as accurately as possible.\n\n"
        f"Context:\n{context_text}\n\n"
        f"Question: {user_query}\n\n"
        f"Answer:"
    )

    # Ask Gemini
    response = gemini_model.generate_content(prompt)
    answer = response.text

    return jsonify({'response': answer})


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
