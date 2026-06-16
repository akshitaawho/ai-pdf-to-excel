import os

from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from services.pdf_parser import extract_text_from_pdf

from fastapi.responses import FileResponse

from services.excel_generator import generate_excel
from services.ai_extractor import extract_structured_data

import shutil

app = FastAPI()

os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/upload")
async def upload_pdf(
    pdf_file: UploadFile = File(...)
):

    file_path = f"uploads/{pdf_file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(pdf_file.file, buffer)

    extracted_text = extract_text_from_pdf(
        file_path
    )

    parsed_data = extract_structured_data(
        extracted_text
    )

    invoice_number = parsed_data.get("invoice_number")

    if not invoice_number:
        invoice_number = "invoice"

    excel_path = f"outputs/{invoice_number}.xlsx"

    generate_excel(
        parsed_data,
        excel_path
    )

    return FileResponse(
        excel_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=f"{invoice_number}.xlsx"
    )