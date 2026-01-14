from . import models
from .database import engine, get_db
from .ai_service import analyze_ticket
from .schemas import AnalyzeCreate, AnalyzeResponse
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List

models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="AI Ticket Summarizer")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/analyze", response_model=AnalyzeResponse)
async def analyze_ticket_endpoint(ticket: AnalyzeCreate, db: Session = Depends(get_db)):
    analysis = analyze_ticket(ticket.ticket_text)

    db_analyze = models.Analyze(
        ticket_text=ticket.ticket_text,
        summary= analysis["summary"]
    )
    
    db.add(db_analyze)
    db.commit()
    db.refresh(db_analyze)
    
    return db_analyze


@app.get("/health")
async def health_check():
    return {"status": "ok"}