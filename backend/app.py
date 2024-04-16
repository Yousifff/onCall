from contextlib import asynccontextmanager

from fastapi import FastAPI
from models import User
from database import SessionDep, create_db_and_tables



@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/admin")
def create_user(user: User, session: SessionDep):

    session.add(user)
    session.commit()
    session.refresh(user)
    

    return user

@app.get("/")
def get_user(session: SessionDep):
    users = session.query(User).all()
    return users
