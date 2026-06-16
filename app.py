from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from services.pdf_parser import extract_text_from_pdf
from services.ai_extractor import extract_structured_data
import shutil

app = FastAPI()

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

    extracted_text = extract_text_from_pdf(file_path)

    structured_data = extract_structured_data(
        extracted_text
    )

    return {
        "filename": pdf_file.filename,
        "structured_data": structured_data
    }