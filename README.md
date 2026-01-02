A lightweight FastAPI microservice that accepts structured PDF files (e.g. bank statements) and extracts key data into a structured JSON response. Designed as a reusable backend component for automation pipelines, data ingestion, and document processing workflows.

🚀 Features

Upload a PDF via REST API

Parse structured PDFs (no OCR)

Extract metadata and tabular transaction data

Return clean, structured JSON

FastAPI + Swagger UI for easy testing

Modular, extensible architecture

Ready for database storage or downstream processing

🛠 Tech Stack

Python 3.12+

FastAPI

Uvicorn

pdfplumber (native PDF parsing)

pandas

SQLite (optional, local testing)

📂 Project Structure
pdf_parser_api/
│
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── parser.py            # PDF parsing logic
│   ├── models.py            # Pydantic schemas
│   └── database.py          # Optional DB logic
│
├── samples/
│   ├── README.md            # Sample folder placeholder
│
├── requirements.txt
├── README.md
├── .gitignore

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/sbrooks25222/pdf-parser-api.git
cd pdf-parser-api

2️⃣ Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Running the API
uvicorn app.main:app --reload


API will be available at:

http://127.0.0.1:8000


Swagger UI:

http://127.0.0.1:8000/docs

🧪 How to Test

Open Swagger UI

Use the POST /parse-pdf endpoint

Upload a structured PDF file

Receive parsed JSON output including:

Statement metadata

Transactions

Dates, amounts, balances

📌 Example Use Cases

Bank statement ingestion

Financial data extraction

Document automation pipelines

Backend services for accounting tools

API-based PDF processing

🔐 Security Notes

No credentials are hardcoded

Uploaded files are processed in-memory

No sensitive data logged

Sample files excluded from version control

📈 Future Improvements

Support for multiple PDF layouts

Excel export endpoint

Authentication & rate limiting

Cloud storage integration (S3 / GCS)

Async batch processing

👤 Author

Shawn Brooks
Python Automation & Web Scraping Developer

GitHub: https://github.com/sbrooks25222

LinkedIn: https://linkedin.com/in/shawn-brooks-2b84818b