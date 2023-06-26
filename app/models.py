from .database import Base
from sqlalchemy import  Column, ForeignKey, Integer, String 
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True )
    name  = Column(String, nullable=False)
    role = Column(String,server_default="trainee " ,nullable=False)
    email= Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
   
class Exercice(Base):
    __tablename__ = "exercices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String,nullable=False)
    userid = Column(Integer, ForeignKey("users.id"))
""" 
class Authentication(Base):
    __tablename__ = """