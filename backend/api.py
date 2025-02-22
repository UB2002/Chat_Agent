from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from server import analyze_data
import os

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/analyze")
async def analyze(query: Query):
    text_answer, viz_path = analyze_data(query.question)
    if viz_path and os.path.exists(viz_path):
        return {"text": text_answer, "visualization": f"http://127.0.0.1:8000/image/{os.path.basename(viz_path)}"}
    return {"text": text_answer, "visualization": None}

@app.get("/image/{image_name}")
async def get_image(image_name: str):
    file_path = image_name  # Assuming images are in the same directory as api.py
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="image/png")
    return {"error": "Image not found"}

# Run with: uvicorn api:app --reload --port 8000