from fastapi import FastAPI 
from routers import split 

app = FastAPI(title="Receipt Splitter API")

app.include_router(
    split.router, 
    prefix="/split", 
    tags=["Split"])