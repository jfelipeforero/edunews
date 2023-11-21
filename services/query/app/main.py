from fastapi import FastAPI
import contextlib
from fastapi.middleware.cors import CORSMiddleware

from api.api_v1 import api
from db_config.config import create_all_tables

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    await create_all_tables()
    yield
    
app = FastAPI(lifespan=lifespan)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api.api_router)

