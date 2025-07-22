from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access them using os.environ or os.getenv
PDF_PATH = "data/medical_book.pdf"
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = "medicalbot"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Load PDF using PyPDF2
print("Loading PDF...")
reader = PdfReader(PDF_PATH)
raw_text = ""

for page in reader.pages:
    text = page.extract_text()
    if text:  # Check if text extraction worked
        raw_text += text + "\n"

print("Text extracted from the PDF.")

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
chunks = text_splitter.split_text(raw_text)

print(f"Text splitted into {len(chunks)} chunks.")

# Generate embeddings
print("Downloading embedding model...")
embedding_model = SentenceTransformer("multi-qa-MiniLM-L6-cos-v1")
embeddings = embedding_model.encode(chunks)

# Upserting vectors into Pinecone
print("Upserting vectors into Pinecone...")
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX_NAME)

vectors = []
for i, (text, emb) in enumerate(zip(chunks, embeddings)):
    vectors.append({
        "id": f"chunk-{i}",
        "values": emb.tolist(),
        "metadata": {"text": text}
    })

# Batch upsert
batch_size = 100
for i in range(0, len(vectors), batch_size):
    index.upsert(vectors=vectors[i:i+batch_size])

print(f"Uploaded {len(vectors)} chunks to Pinecone index '{PINECONE_INDEX_NAME}'.")
