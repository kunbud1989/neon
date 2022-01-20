import json
from optparse import Option
from unittest import result
from fastapi import APIRouter, Body, Query, Response
from typing import Optional
from apps.controllers.RendiController import ControllerRendi as Rendi

router = APIRouter()

input_create_data = json.dumps({
    "loanid": None,
    "loan_type": None,
    "loan_status": None,
    "loan_amount": None,
    "loan_tenure": None,
    "interest": None,
    "cif": None,
    "idno": None,
    "fname": None,
    "lname": None,
    "dob": None,
    "gender": None,
    "marital_status": None,
    "income": None,
    "phone": None,
    "email": None,
    "isphoneverified": None,
    "isemailverified": None,
    "createdate": None,
    "updatedate": None,
    "source": None,
}, indent = 2)


update_data= json.dumps({
    "fname": 'Rendi',
    "lname": 'Salim',
    "dob": "24/05/1998",
    "gender": "Male",
    "marital_status": "Single",
    "income": "150000000",
    "phone": "111-111-111",
    "email": 'r.salim@gmail.com'
})


@router.get("/get_borrower_by_status")
async def read_data_by_status(response: Response, 
                                                loan_status:int,
                                                loan_type:Optional[int]=None,
                                                limit:Optional[int]=None):
    result = Rendi.read_data_by_status(loan_status=loan_status, loan_type=loan_type, limit=limit)
    response.status_code = result.status
    return result

@router.post('/append_borrower_data')
async def insert_data_by_loanid(response: Response, input_data = Body(..., example=input_create_data)):
    result = Rendi.insert_data_by_loanid(input_data = input_data)
    return result

@router.delete('/delete_borrower_data')
async def delete_data_by_idno(response: Response, id_no:Optional[str]=None):
    result = Rendi.delete_data_by_idno(id_no = id_no)
    return result

@router.put('/update_borrower_data')
async def update_demography_data(response: Response, id_no:str, input_data = Body(..., example=update_data)):
    result = Rendi.update_demography_data(id_no = id_no, update_data = input_data)
    return result