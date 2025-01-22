from pydantic import BaseModel


class TokenSchema(BaseModel):
    pass


class UserInSchema(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str


class User(UserInSchema):
    id: int
    is_staff: bool = False
    is_active: bool = True
    is_superuser: bool = False
