from datetime import date
import email
from pydantic import BaseModel
from typing import Optional, List


class RequestCIF(BaseModel):
    cif: str = None


class CIF(BaseModel):
    loanid: str = None
    cif: str  = None
    tenor: int  = None
    amount: int  = None
    limit: int  = None
    type: int = None
    status: int = None
    interest: int = None
    idnumber: str = None
    firstname: str = None
    lastname: str = None
    dob: date = None
    gender: str = None
    maritalstatus: str = None
    income: int = None
    phone: str = None
    email: str = None
    phoneverified: int = None
    emailverified: int = None
    createdate: date = None
    updatedate: date = None
    source: str = None



class ResponseCIF(BaseModel):
    cif_list: List[CIF]