import json
from fastapi import APIRouter, Body, Response
from apps.controllers.WillyController import ControllerWilly as loan

router = APIRouter()


@router.get("/get_risky_user/{risky}")
async def get_risky_user(response: Response, risky:int = 0):
    result = loan.get_risky_user(risky)
    return result


input_loanid = json.dumps({
    "loanid": "100002",
}, indent=2)
@router.post("/get_user_by_loandid")
async def get_user_by_loanid(response: Response, input_data=Body(..., example=input_loanid)):
    result = loan.get_user_by_loanid(input_data=input_data)
    response.status_code = result.status
    return result


@router.put("/test_put")
async def put_test():
    
    return {"messages": "WIP"}

@router.delete("/test_delete")
async def delete_test():

    return {"messages": "WIP"}
