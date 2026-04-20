from pydantic import BaseModel
from datetime import date, time

class Post(BaseModel):
    assignment: str
    description: str
    class_name: str
    date: date # datetime obj
    time: time 
    pals_amount: int
    pals_users: list[str]

class PostWithID(Post):
    user_id: str