from pydantic import BaseModel
from typing import Optional, List


class RequestCIF(BaseModel):
    cif: str = None

class RequestLoanStatus(BaseModel):
    loan_status: int = None
    loan_type: int = None

class CIF(BaseModel):
    loanid: str = None
    cif: str  = None
    tenor: int  = None
    amount: int  = None
    limit: int  = None

class Status(BaseModel):
    loanid: str = None
    idno: str = None
    fname: str = None
    lname: str = None
    gender: str = None
    marital_status: str = None
    income: int = None
    age: int = None
    loan_type: str = None
    loan_amount: int = None
    loan_tenure: int = None
    interest: int = None
    

class ResponseLoanStatus(BaseModel):
    status_list: List[Status]

class ResponseCIF(BaseModel):
    cif_list: List[CIF]