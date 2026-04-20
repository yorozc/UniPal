from database.db_conn import get_unipal_posts
from models.pal_post import Post, PostWithID
from bson import ObjectId
from fastapi import HTTPException
from pymongo import ReturnDocument

class PalPostService:
    def __init__():
        pass

    def return_all_posts() -> list[PostWithID]:
        posts = []
        