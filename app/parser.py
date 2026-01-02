import pdfplumber
from typing import Dict, Any

def parse_pdf_to_structured_data(file_path: str) -> Dict[str, Any]:
    """
    MVP parser:
    - Extracts full text from the PDF
    - Returns structured JSON (simple, but portfolio-ready)
    Later we’ll upgrade this to extract specific fields + tables.
    """
    pages_text = []

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            pages_text.append(text)

    full_text = "\n\n".join(pages_text).strip()

    return {
        "pages": len(pages_text),
        "text": full_text
    }
