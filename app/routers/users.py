from sqlalchemy.orm import Session
from  ..database import SessionLocal, engine,get_db
from .. import  models, schemas,utils
from fastapi import FastAPI, Depends,Response,status,HTTPException,APIRouter

router =APIRouter(
  tags=["Users"]

)


@router.get('/users')
def  get_all_users(db: Session = Depends(get_db)):
    users= db.query(models.User).filter(models.User.role != "coach" ).all()
    return users
@router.get("/user/{id}")
def get_user_by_id(id : int,db: Session = Depends(get_db) ):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not")
    return user 

@router.post('/users', status_code=status.HTTP_201_CREATED,response_model=schemas.UserCreationResponse)
def create_user(user : schemas.User,db: Session = Depends(get_db)):
    hashed_password=utils.hash(user.password)
    user.password=hashed_password
    new_user=models.User(**dict(user))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.delete('/users/{id}')
def delete_user(id :int ,db: Session= Depends(get_db)):
    deleted_user = db.query(models.User).filter(models.User.id == id)
    if deleted_user.first() == None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id : {id} doesn't exist")
    try:
        deleted_user.delete(synchronize_session=False)
    except:
       raise HTTPException(status_code =status.HTTP_401_UNAUTHORIZED,detail ="cannot delete a user having exercices")
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/user/{id}")
def update_uer_information( user : schemas.User,id:int , db : Session = Depends(get_db)):
   updated_user = db.query(models.User).filter(models.User.id ==id)
   if updated_user.first() ==None:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= f"user with id = {id} not found")
   updated_user.update(user.dict(),synchronize_session=False)
   db.commit
   return {"data": updated_user.first()}
