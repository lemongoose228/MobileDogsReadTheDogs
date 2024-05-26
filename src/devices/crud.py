from sqlalchemy.orm import Session
from devices import models, schemas
import uuid
from typing import Optional

def create_collar(db: Session, dog: schemas.CreateDog) -> Optional[models.dogsT]:
    collar_token = str(uuid.uuid4())[:8]
    db.dog = models.dogsT(name=dog.name, collar_id=dog.collar_id, collar_token=collar_token)
    db.add(db.dog)
    db.commit()
    db.refresh(db.dog)
    return db.dog

def find_collar(db: Session, collar_id: str) -> Optional[models.dogsT]:
    dog = db.query(models.dogsT).filter_by(collar_id=collar_id).first()
    return dog
