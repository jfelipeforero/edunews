from typing import Dict, Any

from sqlalchemy import desc, update
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from models.query import Query


"""
"""
class QueryRepository: 
    
    def __init__(self, sess: AsyncSession | Session):
        self.sess: AsyncSession | Session = sess
    

    """
    Inserts a query into the database(queries table)
    """
    async def create_query(self, query: Query) -> Query | None: 
        try: 
            sql = Query(
                name=query.name,
                description=query.description,
                username=query.username,
                country_code=query.country_code,
                year=query.year,
                indicator_code=query.indicator_code,
                comment=query.comment
            )  
            await self.sess.add(sql)
            await self.sess.commit()
            await self.sess.refresh(sql)
        except Exception as e:
            print(f"Error creating query: {e}")
            return None  
        return sql


    """
    Asynchronously returns the query associated with the id provided.
    """
    async def get_query_by_id(self, id: int): 
        try:
            q = await self.sess.execute(select(Query).where(Query.id == id)) 
            return q.scalars().all()
        except Exception as e:
            print(f"Error getting query by id: {e}")
            return None


    """
    Selects and returns the queries that are currently stored in the database.
    """
    async def get_all_queries(self):
        try:
            q = await self.sess.execute(select(Query).order_by(desc(Query.publication_date)))
            return q.scalars().all()
        except Exception as e:
            print(f"Error getting all queries: {e}")
            return None

    """
    Selects and returns all the queries that are currently associated with the 
    username provided by the request
    """
    async def get_by_username(self, username: str): 
        try:
            q = await self.sess.execute(select(Query).where(Query.username == username).order_by(desc(Query.publication_date))) 
            return q.scalars().all()
        except Exception as e:
            print(f"Error getting queries by username: {e}")
            return None

    """
    Returns either true or false if the update was successful.
    """
    async def update_query(self, id: int, details: Dict[str, Any]) -> bool: 
        try:
            sql = update(Query).where(Query.id == id).values(**details)
            sql.execution_options(synchronize_session="fetch")
            await self.sess.execute(sql)
            await self.sess.commit()
        except Exception as e:
            print(f"Error updating query: {e}")
            return False 
        return True
