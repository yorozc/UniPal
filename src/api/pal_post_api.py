from models.pal_post import Post, PostWithId
from fastapi import APIRouter
from services.pal_post_service import PalPostService

palpost_api = APIRouter()

@palpost_api.get("/all") # prefix = /api/posts
async def all_posts() -> list[PostWithId]:
    posts = PalPostService.return_all_posts()
    return posts

@palpost_api.get("/{post_id}")
async def get_post(post_id: str) -> PostWithId:
    return PalPostService.get_post_by_ID(post_id)

@palpost_api.delete("/{post_id}")
async def delete_post(post_id: str):
    return PalPostService.delete_post_by_ID(post_id)
    