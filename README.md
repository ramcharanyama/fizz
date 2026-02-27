Deployed link : https://mask-it-ai.vercel.app/

# PrivacyShield — Multi-Modal PII Redaction System

A multi-modal AI-driven PII redaction framework that automatically detects
and sanitizes sensitive information from text, PDFs, images, audio, and video.

## Features

- Text redaction using Regex + spaCy NER
- PDF redaction (text-based and scanned)
- Image redaction with bounding box masking
- Audio redaction with beep replacement
- Video redaction with face blur and audio masking
- 4 redaction strategies: Mask, Tag, Anonymize, Hash
- REST API via FastAPI
- Web dashboard via Streamlit
- Downloadable redacted files with audit logs

## Tech Stack

- Python 3.9+
- spaCy, Transformers
- EasyOCR, Tesseract
- PyMuPDF, pdfplumber
- OpenAI Whisper
- OpenCV, MoviePy
- FastAPI, Streamlit
- Faker, Pytest

## Installation
```bash
git clone https://github.com/yourname/privacyshield.git
cd privacyshield
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Usage

**Run API:**
```bash
uvicorn main:app --reload
```

**Run Dashboard:**
```bash
streamlit run dashboard.py
```

**CLI:**
```bash
python redact.py --input file.pdf --strategy mask
```

## Redaction Strategies

| Strategy   | Description                        |
|------------|------------------------------------|
| Mask       | Replaces PII with ████             |
| Tag        | Replaces with [EMAIL], [PHONE] etc |
| Anonymize  | Replaces with synthetic fake data  |
| Hash       | Irreversible cryptographic hash    |

## Supported Formats

| Format | Method         |
|--------|----------------|
| TXT    | Regex + NLP    |
| PDF    | PyMuPDF + OCR  |
| Image  | EasyOCR        |
| Audio  | Whisper + beep |
| Video  | OpenCV + Whisper|

## Compliance

GDPR · HIPAA · DPDP Act 2023
