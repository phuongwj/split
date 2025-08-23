from fastapi import FastAPI 
from routes import split 

app = FastAPI(title="Receipt Splitter API")

# app.include_router(split.router, prefix="/split", tags)