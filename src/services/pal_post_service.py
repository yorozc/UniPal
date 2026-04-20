from database.db_conn import palpost_coll
from models.pal_post import Post, PostWithID
from bson import ObjectId
from fastapi import HTTPException
from pymongo import ReturnDocument

class PalPostService:
    def __init__():
        pass

    def return_all_posts() -> list[PostWithID]:
        posts = []
        for post in palpost_coll.find():
            post["id"] = str(post["_id"])
            del post["_id"]
            posts.append(PostWithID(post))
        return posts

        