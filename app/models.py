from .database import Base
from sqlalchemy import  Column, ForeignKey, Integer, String ,Boolean
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    role = Column(String, server_default="coachee", nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    coachId = Column(Integer, ForeignKey("users.id"))




class Exercice(Base):
    __tablename__ = "exercices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String,nullable=False)
    state= Column(Boolean,nullable=False,server_default="false")
    userid = Column(Integer, ForeignKey("users.id"))
 
