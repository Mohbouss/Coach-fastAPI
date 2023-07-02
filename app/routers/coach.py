from sqlalchemy.orm import Session
from  ..database import SessionLocal, engine,get_db

from .. import  models, schemas,utils
from fastapi import FastAPI, Depends,Response,status,HTTPException,APIRouter
router= APIRouter(
     tags=["Coachs"]
)


@router.get('/coachs')
def get_all_coach(db: Session = Depends(get_db)):
    
    coachs= db.query(models.Coach).all()
    return coachs

@router.get('/coachs/{id}')
def  get_a_specific_coach(id:int ,db: Session = Depends(get_db)):
    users= db.query(models.Coach).filter(models.Coach.id == id).first()
    return users

@router.post('/coachs', status_code=status.HTTP_201_CREATED,response_model=schemas.UserCreationResponse)
def create_coash(user : schemas.Coach,db: Session = Depends(get_db)):
    hashed_password=utils.hash(user.password)
    user.password=hashed_password
    new_user=models.Coach(**dict(user))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
@router.delete('/coachs/{id}')
def delete_coach(id :int ,db: Session= Depends(get_db)):
    deleted_user = db.query(models.Coach).filter(models.Coach.id == id)
    if deleted_user.first() == None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id : {id} doesn't exist")
    try:
        deleted_user.delete(synchronize_session=False)
    except:
       raise HTTPException(status_code =status.HTTP_401_UNAUTHORIZED,detail ="cannot delete a user having exercices")
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)