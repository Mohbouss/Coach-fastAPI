from sqlalchemy.orm import Session
from ..database import SessionLocal, engine,get_db
from .. import  models, schemas,utils
from fastapi import FastAPI, Depends,Response,status,HTTPException,APIRouter

router= APIRouter(
  tags=["Exercices"]
)



##get exercices
@router.get('/exercices')
def get_all_exercices(db : Session =Depends(get_db)):
 exercices =db.query(models.Exercice).all()
 return exercices  
##read task with specific id 
@router.get('/exercices/{id}')
def get_task_state(id :int,db : Session =Depends(get_db)):
 exercice =db.query(models.Exercice).filter(models.Exercice.userid == id).all()
 return exercice  
##create exercices   
@router.post('/exercice', status_code=status.HTTP_201_CREATED,response_model= schemas.exerciceCreationResponse )
def create_exercice(exercice: schemas.Exercice,db : Session =Depends(get_db) ):
    new_exercice =models.Exercice(**dict(exercice))
    db.add(new_exercice)
    db.commit()
    db.refresh(new_exercice)
    return new_exercice

##delete exercices

@router.delete('/exercice/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int,db : Session =Depends(get_db)):
    deleted_task=db.query(models.Exercice).filter(models.Exercice.id == id)
    if deleted_task.first() == None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"exercices with id: {id} not found")
    
    deleted_task.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
