from fastapi import APIRouter, Depends
from apis.v1 import router_user   
from apis.v1 import router_blog

api_router = APIRouter()

api_router.include_router(router_user.router, prefix="/user", tags=["user"])
api_router.include_router(router_blog.router, prefix="/blog", tags=["blog"])
