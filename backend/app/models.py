from sqlalchemy import Column, Integer, String, Text, DateTime, ARRAY
from datetime import datetime
from .database import Base

class Analyze(Base): 
    __tablename__ = "Analyze"
    id = Column(Integer, primary_key=True, index=True)
    ticket_text = Column(Text, nullable=False)
    summary = Column(Text, nullable=False)




'''
model.py - talks to database.py

class Ticket(Base) means Ticket is child class of Base called inhertance, which means copying superpower of Base to Ticket

In OOP - 
- Parent(Base) - Has special methods ans rules built in (like " I know how to talk to database")
- Child(Ticket) - Automatically gets all the features of the parent

__tablename__ = name of the table in the database

'''