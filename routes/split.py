from fastapi import FastAPI
from models.bill import Bill
from services.split_service import split_bill

app = FastAPI()

@app.post("/")
def split_bill_endpoint(bill: Bill):
    result = split_bill(bill)
    return {"results": result}