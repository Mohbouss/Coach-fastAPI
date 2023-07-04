from sqlalchemy.orm import Session
from  ..database import SessionLocal, engine,get_db

from .. import  models, schemas,utils
from fastapi import FastAPI, Depends,Response,status,HTTPException,APIRouter

router =APIRouter(
  tags=["Users"]

)
""" coach """


""" @router.get('/coachs')
def get_all_coach(db: Session = Depends(get_db)):
    
    coachs= db.query(models.Coach).all()
    return coachs """
@router.get('/users')
def get_coach(db: Session = Depends(get_db)):
    users= db.query(models.User).filter(models.User.role == "coach").all()
    return users
@router.get('/user/{id}')
def  get_a_specific_coach(id:int ,db: Session = Depends(get_db)):
    users= db.query(models.User).filter(models.User.id == id).first()
    return users

@router.get("/users/{id}")
def get_all_coachees_for_specific_coach(id : int,db: Session = Depends(get_db) ):
    user = db.query(models.User).filter(models.User.coachId == id).all()
    if not user :
            return   {"message": "No users found."}
    return user 


@router.post('/users', status_code=status.HTTP_201_CREATED ) 
def create_coash(user : schemas.User,db: Session = Depends(get_db)):
    check_user =db.query(models.User).filter(models.User.email == user.email)
    if check_user.first():
      raise HTTPException(status_code =status.HTTP_401_UNAUTHORIZED,detail ="this user exist")
 
    hashed_password=utils.hash(user.password)
    user.password=hashed_password
    new_user=models.User(**dict(user))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.delete('/users/{id}')
def delete_coach(id :int ,db: Session= Depends(get_db)):
    deleted_user = db.query(models.User).filter(models.User.id == id)
    if deleted_user.first() == None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id : {id} doesn't exist")
    try:
        deleted_user.delete(synchronize_session=False)
    except:
       raise HTTPException(status_code =status.HTTP_401_UNAUTHORIZED,detail ="cannot delete a user having exercices")
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)









@router.put("/coachees/{id}")
def update_User_information( user : schemas.User,id:int , db : Session = Depends(get_db)):
   updated_user = db.query(models.User).filter(models.User.id ==id)
   if updated_user.first() ==None:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"user with id = {id} not found")
   updated_user.update(user.dict(),synchronize_session=False)
   db.commit()
   return {"data": updated_user.first()}
