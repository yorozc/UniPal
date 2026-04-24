from database.db_conn import palpost_coll
from models.pal_post import Post, PostWithId
from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException
from pymongo import ReturnDocument

class PalPostService:
    def __init__():
        pass

    # returns all posts with ID
    def return_all_posts() -> list[PostWithId]:
        posts = []
        for post in palpost_coll.find():
            post["id"] = str(post["_id"]) # post specific id
            del post["_id"]
            post["user_id"] = str(post["user_id"]) # post's author
            post["pals_users"] = [str(user) for user in post["pals_users"]] # users who reserve the post
            posts.append(PostWithId(**post))
        return posts

    def get_post_by_ID(post_id: str) -> PostWithId:
        try:
            post_response = palpost_coll.find_one({"_id": ObjectId(post_id)})
        except InvalidId:
            raise HTTPException(status_code=422, detail="Not a valid Id")
        
        if post_response is None:
            raise HTTPException(status_code=404, detail="Post not found")
        
        # change id to str (ObjectID -> str)
        post_response["id"] = str(post_response.pop("_id"))
        post_response["pals_users"] = [str(x) for x in post_response.get("pals_users", [])]
        post_response["user_id"] = str(post_response["user_id"])
        return PostWithId(**post_response)