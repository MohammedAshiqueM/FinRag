from backend.apps.ingestion.services.chunker.factory import get_chunker


pages = [
    """
    Apple Inc. reported strong revenue growth during the fiscal year.
    The company experienced increased demand for its products and services.
    Operating income also increased compared with the previous year.
    """,

    """
    Apple identified several risks in its annual report.
    These risks include supply chain disruptions and geopolitical uncertainty.
    The company also faces competition in global markets.
    """
]


chunker = get_chunker()

chunks = chunker.chunk(pages)

for chunk in chunks:
    print("=" * 80)
    print("CHUNK INDEX:", chunk.metadata["chunk_index"])
    print("PAGE:", chunk.metadata["page"])
    print("TEXT:")
    print(chunk.text)