from fastapi import FastAPI
import os

app = FastAPI(title="AttendAI 2.0 - Meta Hackathon")

@app.get("/")
def home():
    return {
        "message": "AttendAI 2.0 is LIVE",
        "hackathon": "Meta Global AI Developer Hackathon",
        "date": "Oct 26 - Nov 4, 2025",
        "status": "Day 1 - Building"
    }

@app.get("/test-llama")
def test_llama():
    # We will add Llama 3.2 call here once you get Fireworks/Baseten key
    return {
        "todo": "Connect Llama 3.2 here",
        "prompt_example": "Summarize attendance: 20 students present, 5 absent on Friday"
    }

@app.post("/attendance/check")
def check_attendance():
    # This is where your anti-proxy logic will go
    return {"step": "Day 2 task - Liveness detection"}
