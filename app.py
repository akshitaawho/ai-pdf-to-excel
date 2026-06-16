from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/upload")
async def upload_pdf(pdf_file: UploadFile = File(...)):
    return {
        "filename": pdf_file.filename,
        "status": "uploaded successfully"
    }