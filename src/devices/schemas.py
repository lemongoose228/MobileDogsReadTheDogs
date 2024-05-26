from pydantic import BaseModel

class Dog(BaseModel):
    name: str

class CreateDog(Dog):
    collar_id: str

class ResponseDog(BaseModel):
    success: bool
    collar_token: str
