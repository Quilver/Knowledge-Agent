import base64
from pathlib import Path
from typing import List, Dict

import fitz  # PyMuPDF

try:
    from PIL import Image
    import pytesseract
except ImportError:
    Image = None
    pytesseract = None


# -----------------------------
# Chunking Utility
# -----------------------------
def chunk_text(text: str, max_size: int = 4000) -> List[str]:
    """Split text into chunks of max_size characters."""
    return [text[i:i + max_size] for i in range(0, len(text), max_size)]


# -----------------------------
# OCR Fallback
# -----------------------------
def ocr_image(pix) -> str:
    """OCR a PyMuPDF pixmap."""
    if Image is None or pytesseract is None:
        return ""

    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return pytesseract.image_to_string(img)


# -----------------------------
# PDF Reader
# -----------------------------
def read_pdf(path: Path) -> str:
    """
    Extract text from a PDF.
    - Uses PyMuPDF for text extraction
    - Falls back to OCR for image-only pages
    """
    doc = fitz.open(path)
    full_text = []

    for page in doc:
        text = page.get_text()

        if text.strip():
            full_text.append(text)
            continue

        # OCR fallback for scanned pages
        pix = page.get_pixmap(dpi=200)
        ocr_text = ocr_image(pix)
        full_text.append(ocr_text)

    return "\n".join(full_text)


# -----------------------------
# Main Tool Entry
# -----------------------------
def read_pdf_tool(path_str: str, chunk_size: int = 4000) -> Dict[str, List[str]]:
    """
    Read a PDF and return chunked text.
    Returns:
        { "filename": ["chunk1", "chunk2", ...] }
    """
    path = Path(path_str)

    if not path.exists():
        raise FileNotFoundError(f"Path not found: {path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("This tool only accepts PDF files")

    text = read_pdf(path)
    chunks = chunk_text(text, chunk_size)

    return {str(path): chunks}
