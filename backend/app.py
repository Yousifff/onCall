from contextlib import asynccontextmanager

from fastapi import FastAPI
from models import User, Weekly
from database import SessionDep, create_db_and_tables
<<<<<<< HEAD
import uvicorn
=======
from datetime import date
from typing import Optional
>>>>>>> 38472b402da789a7b1086722572511861099c89d


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/user")
def create_user(user: User, session: SessionDep):

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@app.post("/weekly")
def create_weekly(start_date: date, end_date: date, session: SessionDep):
    weekly = Weekly(start_date=start_date, end_date=end_date)
    session.add(weekly)
    session.commit()
    session.refresh(weekly)
    return weekly


@app.get("/")
def get_user(session: SessionDep):
    users = session.query(User).all()
    return users


