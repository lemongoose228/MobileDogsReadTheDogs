import users.crud as crud
import users.schemas as schemas
import users.exceptions as exceptions
from dependecies import session
from database import DBSession

from fastapi import APIRouter, Depends

router = APIRouter()

@router.post("/user/registr", response_model=schemas.ResponseUser)
async def UserRegistration(user: schemas.CreateUser, db: DBSession = Depends(session)):
    if crud.find_user(db, user.login):
        raise exceptions.BusyLogin()
    new_user = crud.create_user(db, user)
    result = schemas.ResponseUser(success=True, accessToken=new_user.accessToken)
    return result

@router.post("/user/login", response_model=schemas.ResponseUserLogin)
async def UserLogin(user: schemas.LoginUser, db: DBSession = Depends(session)):

    if not crud.find_user(db, user.login):
        raise exceptions.WrongLogin()
    if not crud.check_password(db, user.login, user.password):
        raise exceptions.WrongPassword()
    if not crud.check_token(db, user.login, user.accessToken):
        raise exceptions.WrongToken()

    result = schemas.ResponseUserLogin(success=True, message="Вы успешно вошли в аккаунт")
    return result


@router.post("/user/creatTask", response_model=schemas.ResponseUser)
async def UserCreateTask(task: schemas.CreateTask, db: DBSession = Depends(session)):
    if not crud1.find_collar(db, task.collar_id):
        raise exceptions1.NotExistCollar()
    if not crud.find_user(db, task.login):
        raise exceptions.WrongLogin()

    result = schemas.ResponseUser(accessToken=task.accessToken, colar_token=task.colar_token, task=task.text)
    return result
