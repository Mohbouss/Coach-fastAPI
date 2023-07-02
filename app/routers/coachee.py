from sqlalchemy.orm import Session
from  ..database import SessionLocal, engine,get_db

from .. import  models, schemas,utils
from fastapi import FastAPI, Depends,Response,status,HTTPException,APIRouter

router =APIRouter(
  tags=["Coachees"]

)


@router.get('/coachees')
def  get_all_coachees(db: Session = Depends(get_db)):
    users= db.query(models.Coachee).all()
    return users
@router.get("/coachee/{id}")
def get_specific_coachee(id : int,db: Session = Depends(get_db) ):
    user = db.query(models.Coachee).filter(models.Coachee.id== id).first()
    if not user :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not")
    return user 
@router.get("/coachees/{id}")
def get_all_coachees_for_specific_coach(id : int,db: Session = Depends(get_db) ):
    user = db.query(models.Coachee).filter(models.Coachee.coachId == id).all()
    if not user :
            return   {"message": "No users found."}
    return user 

@router.post('/coachees', status_code=status.HTTP_201_CREATED,response_model=schemas.UserCreationResponse)
def create_coashee(user : schemas.Coachee,db: Session = Depends(get_db)):
    hashed_password=utils.hash(user.password)
    user.password=hashed_password
    new_user=models.Coachee(**dict(user))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.delete('/coachees/{id}')
def delete_coachee(id :int ,db: Session= Depends(get_db)):
    deleted_user = db.query(models.Coachee).filter(models.Coachee.id == id)
    if deleted_user.first() == None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id : {id} doesn't exist")
    try:
        deleted_user.delete(synchronize_session=False)
    except:
       raise HTTPException(status_code =status.HTTP_401_UNAUTHORIZED,detail ="cannot delete a user having exercices")
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/coachees/{id}")
def update_coachee_information( user : schemas.Coachee,id:int , db : Session = Depends(get_db)):
   updated_user = db.query(models.Coachee).filter(models.Coachee.id ==id)
   if updated_user.first() ==None:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"user with id = {id} not found")
   updated_user.update(user.dict(),synchronize_session=False)
   db.commit()
   return {"data": updated_user.first()}
