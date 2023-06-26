from pydantic import BaseModel,EmailStr

class Exercice(BaseModel):
    name: str
    userid: int 

class User(BaseModel):
    name:  str
    email:EmailStr
    password:str
    role :str 
class UserCreationResponse(BaseModel):
    name:str
    password:str
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
    password:str
    role:str
