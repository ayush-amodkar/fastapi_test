from fastapi import APIRouter, Depends
from apis.v1 import router_user   

api_router = APIRouter()

api_router.include_router(router_user.router, prefix="/user", tags=["user"])