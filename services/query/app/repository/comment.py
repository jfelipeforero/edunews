from typing import Dict, Any, List

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from models.query import Comment


class CommentRepository: 
    
    def __init__(self, sess: AsyncSession | Session):
        self.sess: AsyncSession | Session = sess
    
    async def create_comment(self, comment: Comment) -> Comment | None: 
        try: 
            sql = Comment(username=comment.username, query_id=comment.query_id, content=comment.content)  
            self.sess.add(sql)
            self.sess.commit()
            self.sess.refresh(sql)
        except Exception as e:
            print(f"Error creating comment: {e}")
            return None  
        return sql

    async def get_comments(self, id: int): 
        try:
            q = await self.sess.execute(select(Comment).where(Comment.query_id == id))
            return q.scalars().all()
        except Exception as e:
            print(f"Error getting comments: {e}")
            return None

