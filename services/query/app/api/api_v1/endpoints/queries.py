from typing import Annotated
from fastapi import APIRouter, HTTPException, Query
from db_config.config import AsyncSessionFactory
from repository.query import QueryRepository
from models.query import Query as QueryI
from schemas.query import QueryBody
from repository.query import QueryRepository
from utils.bigquery import get_all_countries, get_all_indicators, get_data, get_multiple

"""
Creates the queries router for handling the different endpoints related
with the Query model
"""
router = APIRouter()

# Creates a query based on the parameters provided by the user in the query builder(client).
@router.post("/create")
async def get_query(body: QueryBody, country_code: Annotated[str, Query()], indicator_code: Annotated[str, Query()], year: Annotated[str | None, Query()] = None):
    try:
        async with AsyncSessionFactory() as sess:
            async with sess.begin():
                repo = QueryRepository(sess)
                query = QueryI(
                    name=body.name,
                    description=body.description,
                    username=body.username,
                    country_code=country_code,
                    year=year,
                    indicator_code=indicator_code
                )
                data = get_data(country_code, indicator_code, year)

                if body.save == "true":
                    await repo.create_query(query)
                return data
    except Exception as e:
        print(f"Error processing create query request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# Returns all the queries in the database
@router.get("/all-queries")
async def get_all_queries():
    try:
        async with AsyncSessionFactory() as sess:
            async with sess.begin():
                repo = QueryRepository(sess)
                return await repo.get_all_queries()
    except Exception as e:
        print(f"Error processing get all queries request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Returns BigQuery data based on the params provided by the user
@router.get("/id/comments")
async def get_multiple(country_code: Annotated[list[str], Query()], indicator: Annotated[str, Query()], year: Annotated[str, Query()]):
    try:
        async with AsyncSessionFactory() as sess:
            async with sess.begin():
                comments = get_multiple(country_code, indicator, year)
                return comments
    except Exception as e:
        print(f"Error processing get multiple request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Returns all the BigQuery indicators for
@router.get("/all-indicators")
async def list_all_indicators():
    try:
        async with AsyncSessionFactory() as sess:
            async with sess.begin():
                return get_all_indicators()
    except Exception as e:
        print(f"Error processing list all indicators request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Returns all the posts associated with the query param 'username'
@router.get("/")
async def get_by_user(username: Annotated[str, Query()]):
    try:
        async with AsyncSessionFactory() as sess:
            async with sess.begin():
                repo = QueryRepository(sess)
                return await repo.get_by_username(username)
    except Exception as e:
        print(f"Error processing get by user request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Returns all the BigQuery countries present in the education database.
@router.get("/all-countries")
async def list_all_countries():
    try:
        async with AsyncSessionFactory() as sess:
            async with sess.begin():
                return get_all_countries()
    except Exception as e:
        print(f"Error processing list all countries request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Returns a query in the database identified by the path param {id}
@router.get("/{id}")
async def get_by_id(id: int):
    try:
        async with AsyncSessionFactory() as sess:
            async with sess.begin():
                repo = QueryRepository(sess)
                return await repo.get_query_by_id(id)
    except Exception as e:
        print(f"Error processing get by id request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

