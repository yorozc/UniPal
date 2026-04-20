from models.pal_post import Post, PostWithId
from fastapi import APIRouter
from services.pal_post_service import PalPostService

palpost_api = APIRouter()

@palpost_api.get("/all") # prefix = /api/posts
async def all_posts() -> list[PostWithId]:
    posts = PalPostService.return_all_posts()
    return posts