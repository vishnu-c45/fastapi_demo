from pydantic import BaseModel, EmailStr


class UserformSchema(BaseModel):
    name: str
    email: str
    message: str
