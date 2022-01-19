import json
from fastapi import APIRouter, Body, Response
from apps.controllers.LoanidController import ControllerLoanid as loan

router = APIRouter()

example_input_cifno = json.dumps({
    "cif": "1",
}, indent=2)

input_loan_status = json.dumps({
    "loan_status": "1",
    "loan_type": "1"
}, indent = 2)


input_loanid = json.dumps({
    "loanid": "100002",
}, indent=2)
@router.post("/get_user_by_loandid")
async def get_user_by_loanid(response: Response, input_data=Body(..., example=input_loanid)):
    result = loan.get_user_by_loanid(input_data=input_data)
    response.status_code = result.status
    return result

