from datetime import date
import email
from pydantic import BaseModel
from typing import Optional, List

class RequestInsertUser(BaseModel):
    risky: int = None

class InsertUser(BaseModel):
    loanid: str = None
    loan_type: int = None
    loan_status: int = None
    loan_amount: int  = None
    loan_tenure: int  = None
    interest: int = None
    cif: Optional[str]  = None
    idno: Optional[str] = None
    fname: Optional[str] = None
    lname: Optional[str] = None
    dob: Optional[date] = None
    gender: Optional[str] = None
    marital_status: Optional[str] = None
    income: Optional[int] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    createdate: Optional[date] = None
    updatedate: Optional[date] = None
    source: str = None

class ResponseInsertUser(BaseModel):
    user_list: List[InsertUser]