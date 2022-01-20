import json
from fastapi import APIRouter, Body, Response
from apps.controllers.WillyController import ControllerWilly as loan

router = APIRouter()


@router.get("/get_risky_user/{risky}")
async def get_risky_user(response: Response, risky:int = 0):
    result = loan.get_risky_user(risky)
    response.status_code = result.status
    return result


input_insert_data = json.dumps({
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
}, indent=2)
@router.post("/insert_user")
async def insert_user(response: Response, input_data=Body(..., example=input_insert_data)):
    result = loan.insert_user(input_data=input_data)
    temp = json.dumps({
        "loanid": "100401",
        "fname": 'Willy',
        "lname": 'Tamba'
    })
    response.status_code = result.status
    return result


@router.put("/test_put")
async def put_test():
    
    return {"messages": "WIP"}

@router.delete("/test_delete")
async def delete_test():

    return {"messages": "WIP"}
