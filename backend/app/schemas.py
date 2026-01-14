from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class AnalyzeCreate(BaseModel): 
    ticket_text: str

class AnalyzeResponse(BaseModel):
    id: int
    ticket_text: str
    summary: str

    class Config:
        from_attributes = True





'''
schemas.py - defines data structure for data exchange between app and user, talks to API user (Frontend or client). It validates the data given by user and provided by the API
BaseModel is a parent class provided by Pydantic library, it checks the data types automatically ( e.g., ensures id is an integer, turns a JSON string "2023-01-01" into a Python datetime object)
'''