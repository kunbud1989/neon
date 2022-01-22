import json
from optparse import Option
from unittest import result
from fastapi import APIRouter, Body, Query, Response
from typing import Optional
from apps.controllers.RendiController import ControllerRendi as Rendi

router = APIRouter()

input_data = json.dumps({
    "loan_type": "1",
    "loan_status": "1",
    "loan_amount": "5000",
    "loan_tenure": "20",
    "interest": "15",
    "cif": "88835",
    "idno": "34567",
    "fname": "Rendi",
    "lname": "Salim",
    "dob": "1998/05/24",
    "gender": "Male",
    "marital_status": "Single",
    "income": 50000,
    "phone": "111-111-111",
    "email": 'r.salim@gmail.com',
    "isphoneverified": 0,
    "isemailverified": 0,
    "createdate": "2022/05/20",
    "updatedate": "2022/05/20",
    "source": "Web",
}, indent = 2)

@router.get("/get_borrower_by_status")
async def read_data_by_status(response: Response, 
                                                loan_status:int,
                                                loan_type:Optional[int]=None,
                                                limit:Optional[int]=None):
    result = Rendi.read_data_by_status(loan_status=loan_status, loan_type=loan_type, limit=limit)
    response.status_code = result.status
    return result


@router.get("/get_borrower_by_status_debug")
async def read_data_by_status_debug(response: Response, 
                                                loan_status:int,
                                                loan_type:Optional[int]=None,
                                                limit:Optional[int]=None):
    result = Rendi.read_data_by_status_debug(loan_status=loan_status, loan_type=loan_type, limit=limit)
    response.status_code = result.status
    return result

@router.get("/get_loan_by_borrower")
async def read_loan_by_borrower(response: Response, cif: str):
    result = Rendi.read_loan_by_borrower(cif= cif)
    response.status_code = result.status
    return result

@router.post('/append_borrower_data')
async def insert_data(response: Response, input_data = Body(..., example=input_data)):
    result = Rendi.insert_data(input_data = input_data)
    return result

@router.delete('/delete_borrower_data')
async def delete_data(response: Response, loanid:Optional[str]=None):
    result = Rendi.delete_data(loanid = loanid)
    return result

@router.put('/update_borrower_data')
async def update_data(response: Response, loanid:str, input_data = Body(..., example=input_data)):
    result = Rendi.update_data(loanid = loanid, update_data = input_data)
    return result