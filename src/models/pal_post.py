from pydantic import BaseModel
from datetime import date, time

class Post(BaseModel):
    name: str
    email: str
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