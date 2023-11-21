from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

"""
Base Query model used for 
"""
class QueryBase(BaseModel):   
    publication_date: datetime = Field(default_factory=datetime.now)
    name: Optional[str] = None
    username: Optional[str] = None
    country_code: Optional[str] = None
    indicator_code: Optional[str] = None 
    year: Optional[int] = None
    comment: Optional[str] = None

"""
Model definition for the comment body used in the queries endpoints for type
checking
"""
    
class QueryBody(QueryBase):
    save: str
    name: Optional[str] = None
    description: Optional[str]
    username: str
    

class QueryInDBBase(QueryBase): 
    class Config:
        from_attributes = True

