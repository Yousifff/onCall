from sqlmodel import SQLModel, Field , Relationship
from datetime import date
from typing import List

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    weekly: List["Weekly"] = Relationship(back_populates="user")

class Weekly(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    start_date: date  # Corrected to use Date data type
    end_date: date    # Corrected to use Date data type
    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="weekly")
    
