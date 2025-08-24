from fastapi import APIRouter
from models.bill import Bill
from services.split_service import split_bill

router = APIRouter()

@router.post("/")
def split_bill_endpoint(bill: Bill):
    result = split_bill(bill)
    return {"results": result}