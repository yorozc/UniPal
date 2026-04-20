from database.db_conn import palpost_coll
from models.pal_post import Post, PostWithId
from bson import ObjectId
from fastapi import HTTPException
from pymongo import ReturnDocument

class PalPostService:
    def __init__():
        pass

    def return_all_posts() -> list[PostWithId]:
        posts = []
        for post in palpost_coll.find():
            post["id"] = str(post["_id"]) # post specific id
            del post["_id"]
            post["user_id"] = str(post["user_id"]) # post's author
            post["pals_users"] = [str(user) for user in post["pals_users"]] # users who reserve the post
            posts.append(PostWithId(**post))
        return posts

        