import json
from fastapi import APIRouter, Body, Response
from apps.controllers.WillyController import ControllerWilly as loan

router = APIRouter()


input_loanid = json.dumps({
    "loanid": "100002",
}, indent=2)
@router.post("/get_user_by_loandid")
async def get_user_by_loanid(response: Response, input_data=Body(..., example=input_loanid)):
    result = loan.get_user_by_loanid(input_data=input_data)
    response.status_code = result.status
    return result

