# AI PDF To Excel Converter

A web application that converts PDF invoices into structured Excel files.

## Features

* Upload PDF invoices
* Extract text from PDFs
* Parse invoice information
* Generate Excel files automatically
* Download Excel output

## Technology Stack

* FastAPI
* Python
* pdfplumber
* pandas
* openpyxl

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Open:

http://127.0.0.1:8000

## Workflow

PDF → Text Extraction → Data Parsing → Excel Generation → Download
