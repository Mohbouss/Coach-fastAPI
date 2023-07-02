from .database import Base
from sqlalchemy import  Column, ForeignKey, Integer, String ,Boolean
from sqlalchemy.orm import relationship
class Coach(Base):
    __tablename__ = "coach"

    id = Column(Integer, primary_key=True, autoincrement=True )
    name  = Column(String, nullable=False)
    role = Column(String,server_default="coach" ,nullable=False)
    email= Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)

class Coachee(Base):
    __tablename__ = "coachee"

    id = Column(Integer, primary_key=True, autoincrement=True )
    name  = Column(String, nullable=False)
    role = Column(String,server_default="coachee" ,nullable=False)
    email= Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    coachId = Column(Integer,ForeignKey(Coach.id),autoincrement=True)
    
class Exercice(Base):
    __tablename__ = "exercices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String,nullable=False)
    state= Column(Boolean,nullable=False,server_default="false")
    userid = Column(Integer, ForeignKey("coachee.id"))
 
