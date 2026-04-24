from pydantic import BaseModel, EmailStr
from datetime import date, time

class Post(BaseModel):
    name: str
    email: EmailStr
    assignment: str
    description: str
    class_name: str
    pals: int
    user_id: str # ObjectID -> str
    pals_users: list[str] # ObjectID -> str
    date: str # datetime obj change later
    time: str # change later
    class_name: str

class PostWithId(Post):
    id: str

class PostUpdate(BaseModel):
    name: str | None
    email: EmailStr | None
    assignment: str | None
    description: str | None
    class_name: str | None
    pals: int | None
    user_id: str # ObjectID -> str
    pals_users: list[str] | list[None] # ObjectID -> str
    date: str | None
    time: str | None
    class_name: str | None