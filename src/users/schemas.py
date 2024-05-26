from pydantic import BaseModel

class User(BaseModel):
    login: str

class CreateUser(User):
    password: str

class Login(User):
    password: str

class ResponseUserLogin(BaseModel):
    success: bool
    accessToken: str

class LoginUser(User):
    password: str
    accessToken: str

class ResponseUserLogin(BaseModel):
    success: bool
    message: str

class CreateTask(BaseModel):
    accessToken: str
    colar_id: str
    task: str
