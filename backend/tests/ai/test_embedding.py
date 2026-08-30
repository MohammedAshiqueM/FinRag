from backend.apps.ai.embedding.factory import get_embedding_service

def main():
    # Example texts to embed
    texts = [
        "Apple Inc. reported strong revenue growth during the fiscal year.",
        "The company identified several risks in its annual report.",
        "Supply chain disruptions and geopolitical uncertainty remain challenges."
    ]

    # Get embedding service based on EMBEDDING_PROVIDER setting
    embedding_service = get_embedding_service()

    # Generate embeddings
    embeddings = embedding_service.embed(texts)

    print("=" * 80)
    print("INPUT TEXTS:")
    for i, text in enumerate(texts, start=1):
        print(f"{i}. {text}")
    print("=" * 80)
    print("EMBEDDINGS (preview):")
    for i, emb in enumerate(embeddings, start=1):
        print(f"Text {i} → Embedding length: {len(emb)}")
        print(f"First 5 values: {emb[:5]}")
        print("-" * 40)


if __name__ == "__main__":
    main()
