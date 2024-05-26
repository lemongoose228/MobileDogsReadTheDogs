import devices.crud as crud
import devices.schemas as schemas
import devices.exceptions as exceptions
from dependecies import session
from database import DBSession
from fastapi import APIRouter, Depends

router = APIRouter()

@router.post("/dogs/registr", response_model=schemas.ResponseDog)
async def DogsRegistration(dog: schemas.CreateDog, db: DBSession = Depends(session)):
    if crud.find_collar(db, dog.collar_id):
        raise exceptions.BusyCollar()
    new_dog = crud.create_collar(db, dog)
    result = schemas.ResponseDog(success=True, collar_token=new_dog.collar_token)
    return result
