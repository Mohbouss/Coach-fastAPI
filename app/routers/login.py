from fastapi import FastAPI, Depends,Response,status,HTTPException,APIRouter
from ..database import get_db
from sqlalchemy.orm  import Session
from .. import   schemas,models,utils
router =APIRouter(

)

@router.post("/login")
def login(user_credentials :schemas.Auth , db: Session = Depends(get_db)):
    password=user_credentials.password

    user=db.query(models.User).filter(models.User.email==user_credentials.email).first()
    if  user ==None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,detail="invalid credentials")
    
    if not utils.verify(user_credentials.password,user.password):    
         raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,detail="invalid credentials")
    
    return user
