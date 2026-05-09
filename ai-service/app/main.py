from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import os

app = FastAPI(title="AI Analysis Service")

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://host.docker.internal:11434")

class AnalysisRequest(BaseModel):
    logType: str
    description: str
    severity: str

class AnalysisResponse(BaseModel):
    analysis: str
    recommendation: str

@app.get("/")
def root():
    return {"service": "AI Analysis Service", "status": "running"}

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_log(request: AnalysisRequest):
    """
    Analyze log using Ollama LLM

    TODO: Implement AI analysis
    1. Build prompt from log data
    2. Call Ollama API
    3. Parse response
    4. Return analysis and recommendations
    """

    # TODO: Replace with actual Ollama call
    prompt = f"""Analyze this log event:
    Type: {request.logType}
    Description: {request.description}
    Severity: {request.severity}

    Provide analysis and recommendations."""

    # Placeholder response
    return AnalysisResponse(
        analysis=f"Analysis for {request.logType}: TODO - Connect to Ollama",
        recommendation="TODO - Implement AI recommendations"
    )

@app.get("/health")
def health():
    return {"status": "healthy"}
