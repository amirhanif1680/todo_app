# fastapi_neon/main.py

from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine
from fastapi_helloworld import settings
from contextlib import asynccontextmanager


class ToDo(SQLModel, Table=True):
    id : int | None = Field(default=None, primary_key=True)
    content : str
   
connection_string = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
) 

engine = create_engine(
    connection_string
)

def create_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("creating Tables..")
    create_tables()
    yield
    
 
app:FastAPI = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}