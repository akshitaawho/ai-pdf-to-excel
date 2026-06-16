

import os

from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from services.pdf_parser import extract_text_from_pdf

from fastapi.responses import FileResponse

from services.excel_generator import generate_excel
from services.ai_extractor import extract_structured_data

from fastapi.staticfiles import StaticFiles

import shutil

app = FastAPI()
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

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

    # saves the uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(pdf_file.file, buffer)

    # extracts the text from the PDF
    extracted_text = extract_text_from_pdf(
        file_path
    )
    # sends the text to AI
    parsed_data = extract_structured_data(
        extracted_text
    )

    document_type = parsed_data.get(
        "document_type",
        "document"
    )

    document_type = document_type.replace(
        " ",
        "_"
    )

    excel_path = f"outputs/{document_type}.xlsx"

    # generates excel sheet
    generate_excel(
        parsed_data,
        excel_path
    )

    # returns the excel sheet
    return FileResponse(
        excel_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=f"{document_type}.xlsx"
    )