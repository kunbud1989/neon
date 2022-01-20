import json
from fastapi import APIRouter, Body, Response
from apps.controllers.RendiController import ControllerRendi as Rendi

router = APIRouter()

input_loan_status = json.dumps({
    "loan_status": "1",
    "loan_type": None,
    "limit": 10
}, indent = 2)


@router.post("/get_active_borrower_from_type_and_status_by_rendi")
async def get_active_borrower_from_type_and_status_by_rendi(response: Response, input_data=Body(..., example=input_loan_status)):
    result = Rendi.get_active_borrower_from_type_and_status_by_rendi(input_data=input_data)
    response.status_code = result.status
    return result
