from datetime import datetime
from typing import List

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, backref, mapped_column, relationship

# Referenced for the creation of the tables based on the models specified 
class Base(DeclarativeBase):
    pass

"""
SQLAlchemy Models definition

"""

class Query(Base):
    __tablename__ = "queries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    publication_date: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.now
    )
    name: Mapped[str] = mapped_column(String(255), nullable=True)  
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    username: Mapped[str] = mapped_column(String(255), nullable=False) 
    country_code: Mapped[str] = mapped_column(String(255), nullable=True)
    indicator_code: Mapped[str] = mapped_column(String(255), nullable=True) 
    year: Mapped[str] = mapped_column(Text, nullable=True) 

    comment: Mapped["Comment"] = relationship(back_populates='query')

class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    query_id: Mapped[int] = mapped_column(ForeignKey("queries.id"))
    query: Mapped["Query"] = relationship(back_populates="comment")

    publication_date: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.now
    ) 
    content: Mapped[str] = mapped_column(String(255), nullable=False)  
