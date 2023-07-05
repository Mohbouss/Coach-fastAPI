from pydantic import BaseModel,EmailStr
from typing import Optional
from sqlalchemy import  Column, ForeignKey, Integer, String ,Boolean

class Exercice(BaseModel):
    name: str
    userid: int 
""" class Coach(BaseModel):
    name:  str
    email:EmailStr
    password:str

    
class Coachee(Coach):
    coachId : int
 """
class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    role : str
    coachId: Optional[int] = None

class UserCreationResponse(BaseModel):
    name:str
    role:str
    class Config:
        orm_mode = True
        

class exerciceCreationResponse(BaseModel):
    name: str
    class Config:
        orm_mode = True

class Auth(BaseModel):
    email:EmailStr
    password:str
class Authout(BaseModel):
    role:str

class UpdateExercise(BaseModel):
    state: bool