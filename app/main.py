from fastapi import FastAPI, Depends,Response,status,HTTPException
from fastapi.params import Body 
from pydantic import BaseModel
from typing import Optional,List
from random import randrange
from . import  models, schemas,utils
from .routers import users,exercices,login
from .database import SessionLocal, engine,get_db
from sqlalchemy.orm import Session
import psycopg2
from psycopg2.extras import RealDictCursor  
import time
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(bind=engine)   
"""  ##CONNECTION WITH DB
while True:
   try:
      conn= psycopg2.connect(host='localhost',database='CoashMe',user='postgres',password='123456', cursor_factory=RealDictCursor)
      cursor = conn.cursor()
      print('datatbse connc was success')
      break
   except Exception as error:
      print("connec failed")
      print('error:',error)
      time.sleep(2)
  """

app.include_router(users.router)
app.include_router(exercices.router)
app.include_router(login.router)