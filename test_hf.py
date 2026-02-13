from huggingface_hub import InferenceClient
import os

client = InferenceClient(token="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")
try:
    # Instead of client.feature_extraction, let's just see where it points
    print(f"Base URL: {client.base_url}")
    # Try to get an embedding
    emb = client.feature_extraction("test text", model="sentence-transformers/all-MiniLM-L6-v2")
    print(f"Embedding length: {len(emb)}")
except Exception as e:
    print(f"Error: {e}")
