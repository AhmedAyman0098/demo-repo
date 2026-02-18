from typing import List
from fastapi import FastAPI,Depends, status, Response,HTTPException, Request
from . import schemas,models, hashing
from pydantic import BaseModel
from .database import engine, get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .hashing import Hash
from .routers import blog, user, authentication

app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)





    

