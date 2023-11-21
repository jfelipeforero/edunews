from fastapi import APIRouter, HTTPException
from db_config.config import AsyncSessionFactory
from repository.comment import CommentRepository
from models.query import Comment
from schemas.comment import CommentBase


"""
Creates the comments router for handling the different endpoints related
with the Comment model
"""
router = APIRouter()

# Creates a comment in the post specified by id
@router.post("/create/{id}")
async def create_comment(req: CommentBase, id: int):
    try:
        async with AsyncSessionFactory() as sess:
            async with sess.begin():
                repo = CommentRepository(sess)
                comment = Comment(username=req.username, query_id=id, content=req.content)
                return await repo.create_comment(comment)
    except Exception as e:
        print(f"Error creating comment: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# Get comment by post id
@router.get("/{id}")
async def get_comments_by_post_id(id: int):
    try:
        async with AsyncSessionFactory() as sess:
            async with sess.begin():
                repo = CommentRepository(sess)
                comments = await repo.get_comments(id)
                return comments
    except Exception as e:
        print(f"Error getting comments by post id: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

