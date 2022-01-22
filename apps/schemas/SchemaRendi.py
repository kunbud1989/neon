from datetime import date
from pydantic import BaseModel
from typing import Optional, List

class Status(BaseModel):
    loanid: str = None
    loan_type: int = None
    loan_status: int = None
    loan_amount: int  = None
    loan_tenure: int  = None
    interest: int = None
    cif: str  = None
    idno: str = None
    fname: str = None
    lname: str = None
    dob: date = None
    gender: str = None
    marital_status: str = None
    income: int = None
    phone: str = None
    email: str = None
    isphoneverified: int = None
    isemailverified: int = None
    createdate: date = None
    updatedate: date = None
    source: str = None


class ResponseLoanStatus(BaseModel):
    status_list: List[Status]
