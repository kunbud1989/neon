import json
from fastapi import APIRouter, Body, Response
from apps.controllers.WillyController import ControllerWilly as loan

router = APIRouter()


@router.get("/get_risky_user/{risky}")
async def get_risky_user(response: Response, risky:int = 0):
    result = loan.get_risky_user(risky)
    response.status_code = result.status
    return result


input_loanid = json.dumps({
    "loanid": "100002",
    "fname": "",
    "lname": ""
}, indent=2)
@router.post("/insert_user")
async def insert_user(response: Response, input_data=Body(..., example=input_loanid)):
    result = loan.insert_user(input_data=input_data)
    response.status_code = result.status
    return result


@router.put("/test_put")
async def put_test():
    
    return {"messages": "WIP"}

@router.delete("/test_delete")
async def delete_test():

    return {"messages": "WIP"}
