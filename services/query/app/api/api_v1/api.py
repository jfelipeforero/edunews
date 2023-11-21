from fastapi import APIRouter

from .endpoints import queries
from .endpoints import comments

"""
Creation of the router including the query and comment router
"""
api_router = APIRouter()
api_router.include_router(queries.router, prefix="/query", tags=["query"])
api_router.include_router(comments.router, prefix="/query/comments", tags=["comment"])
