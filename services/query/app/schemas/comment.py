from datetime import datetime
from pydantic import BaseModel, Field


"""
Definition of pydantic Models for Comment  
"""

# Contains the base properties of the comment model..
class CommentBase(BaseModel):    
    publication_date: datetime = Field(default_factory=datetime.now)
    username: str 
    content: str


class CommentCreate(CommentBase):
    pass

class CommentInDBBase(CommentBase): 
    class Config:
        from_attributes = True

