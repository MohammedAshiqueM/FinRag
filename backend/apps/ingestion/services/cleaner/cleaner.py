import re

class TextCleaner():
    """
    class for cleaning the extracted data from docs
    currently only using one cleaning strategy (so there is no abstract BaseCleaner and factory method)
    """
    def clean(self, text: str) -> str:

        if not text:
            return ""

        # Normalize line endings
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")

        # Replace tabs with spaces
        text = text.replace("\t", " ")

        # Remove trailing/leading whitespace from every line
        lines = [
            line.strip()
            for line in text.split("\n")
        ]

        # Remove completely empty lines at the beginning/end
        text = "\n".join(lines).strip()

        # Collapse multiple spaces
        text = re.sub(r"[ ]{2,}", " ", text)

        # Collapse excessive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text