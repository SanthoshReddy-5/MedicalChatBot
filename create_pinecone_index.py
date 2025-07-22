from pinecone import Pinecone,ServerlessSpec
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Initialize Pinecone
pc=Pinecone(api_key=PINECONE_API_KEY)

# Define index name and configuration
index_name = "medicalbot"

# Check if the index already exists
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,  # This depends on your embedding model
        metric="cosine",
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )
    print(f"Index '{index_name}' created successfully.")
else:
    print(f"Index '{index_name}' already exists.")
