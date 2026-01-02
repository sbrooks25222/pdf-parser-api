import json
import os
from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session

from .database import Base, engine, SessionLocal
from .models import ParsedDocument
from .schemas import ParseResponse
from .parser import parse_pdf_to_structured_data

Base.metadata.create_all(bind=engine)

app = FastAPI(title="PDF Parser API", version="1.0")

UPLOAD_DIR = "output"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/parse-pdf", response_model=ParseResponse)
async def parse_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    save_path = os.path.join(UPLOAD_DIR, file.filename)

    contents = await file.read()
    with open(save_path, "wb") as f:
        f.write(contents)

    try:
        extracted = parse_pdf_to_structured_data(save_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse PDF: {str(e)}")

    doc = ParsedDocument(
        filename=file.filename,
        doc_type="generic",
        extracted_json=json.dumps(extracted, ensure_ascii=False)
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)

    return ParseResponse(
        id=doc.id,
        filename=doc.filename,
        doc_type=doc.doc_type,
        extracted=extracted,
        created_at=doc.created_at
    )
