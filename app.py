from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI PDF To Excel is running"}