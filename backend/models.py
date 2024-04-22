from sqlmodel import SQLModel, Field , Relationship
from datetime import date
from typing import List

class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    start_date: str
    end_date: str
    #weekly: List["Weekly"] = Relationship(back_populates="user")

'''class Weekly(SQLModel, table=True):
    id: int = Field(primary_key=True)
    start_date: date
    end_date: date
    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="weekly")'''


    
