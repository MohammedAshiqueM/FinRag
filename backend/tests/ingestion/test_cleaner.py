

from backend.apps.ingestion.services.cleaner.cleaner import TextCleaner


def main():
    cleaner = TextCleaner()

    # Example messy text (tabs, multiple spaces, mixed line endings, excessive blank lines)
    raw_text = """
        Apple Inc.   reported strong revenue growth during the fiscal year.\r\n
        The company experienced increased demand for its products and services.\t
        Operating income also increased compared with the previous year.\n\n\n

        Apple identified several risks in its annual report.\r\n
        These risks include supply chain disruptions and geopolitical uncertainty.\n
           The company also faces competition in global markets.\t\t
    """

    print("=" * 80)
    print("RAW TEXT:")
    print(raw_text)
    print("=" * 80)

    cleaned_text = cleaner.clean(raw_text)

    print("CLEANED TEXT:")
    print(cleaned_text)
    print("=" * 80)


if __name__ == "__main__":
    main()
