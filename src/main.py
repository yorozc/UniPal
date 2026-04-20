from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from api.pal_post_api import palpost_api

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# external api
app.include_router(palpost_api, prefix="/api/posts", tags=["posts"])

app.state.templates = Jinja2Templates(directory="templates")

template = Jinja2Templates(directory="templates")

