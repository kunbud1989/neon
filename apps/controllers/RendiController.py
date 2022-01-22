from cmath import log
from urllib import request
from pydantic import NoneIsAllowedError, ValidationError
from turtle import update
from apps.helper import Log
from apps.schemas import BaseResponse
from apps.schemas.SchemaRendi import ResponseLoanStatus
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
from apps.models.LoanModel import Loan
from apps.models.BorrowerModel import Borrower

SALT = PARAMS.SALT.salt


class ControllerRendi(object):
    @classmethod
    def read_data_by_status(cls, loan_type, loan_status, limit):
        result = BaseResponse()
        result.status = 400

        try:
            if limit is None:
                limit = Loan.count('loanid')

            if (loan_status is not None) and (loan_type is not None):

                if loan_status not in range (Loan.min('loan_status'), Loan.max('loan_status')+1): 
                    result.message = f"No loan status above {Loan.max('loan_status')} or below {Loan.min('loan_status')}"
                    Log.info(result.message)

                elif loan_type not in range (Loan.min('loan_type'), Loan.max('loan_type')+1):
                    result.message = f"No loan type above {Loan.max('loan_type')} or below {Loan.min('loan_type')}"
                    Log.info(result.message)

                else:
                    data = Loan.where('loan_status', '=', loan_status).where('loan_type', '=', loan_type).limit(limit).get().serialize()
                    result.status = 200
                    result.message = "Success"
                    result.data = encoder_app(ResponseLoanStatus(**{"status_list": data}).json(), SALT)
                    Log.info(result.message)

            elif loan_status is not None:
                if loan_status not in range (Loan.min('loan_status'), Loan.max('loan_status')+1): 
                    result.message = f"No loan status above {Loan.max('loan_status')} or below {Loan.min('loan_status')}"
                    Log.info(result.message)

                else:
                    data = Loan.where('loan_status', '=', loan_status).limit(limit).get().serialize()
                    result.status = 200
                    result.message = "Success"
                    result.data = encoder_app(ResponseLoanStatus(**{"status_list": data}).json(), SALT)
                    Log.info(result.message)

            else:
                data = Loan.limit(limit).get().serialize()
                result.status = 200
                result.message = "Success Query Without Filter"
                result.data = encoder_app(ResponseLoanStatus(**{"status_list": data}).json(), SALT)
                Log.info(result.message)

        except ValidationError:
            m = 'Wrong data type!'
            Log.error(m)
            result.status = 400
            result.message = str(m)


        except Exception:
            m = "Error"
            Log.error(m)
            result.status = 400
            result.message = str(m)

        return result

    @classmethod
    def read_data_by_status_debug(cls, loan_type, loan_status, limit):
        result = BaseResponse()
        result.status = 400

        try:
            if limit is None:
                limit = Loan.count('loanid')

            if (loan_status is not None) and (loan_type is not None):

                if loan_status not in range (Loan.min('loan_status'), Loan.max('loan_status')+1): 
                    result.message = f"No loan status above {Loan.max('loan_status')} or below {Loan.min('loan_status')}"
                    Log.info(result.message)

                elif loan_type not in range (Loan.min('loan_type'), Loan.max('loan_type')+1):
                    result.message = f"No loan type above {Loan.max('loan_type')} or below {Loan.min('loan_type')}"
                    Log.info(result.message)

                else:
                    data = Loan.where('loan_status', '=', loan_status).where('loan_type', '=', loan_type).limit(limit).get().serialize()
                    result.status = 200
                    result.message = "Success"
                    result.data = ResponseLoanStatus(**{"status_list": data})
                    Log.info(result.message)

            elif loan_status is not None:
                if loan_status not in range (Loan.min('loan_status'), Loan.max('loan_status')+1): 
                    result.message = f"No loan status above {Loan.max('loan_status')} or below {Loan.min('loan_status')}"
                    Log.info(result.message)

                else:
                    data = Loan.where('loan_status', '=', loan_status).limit(limit).get().serialize()
                    result.status = 200
                    result.message = "Success"
                    result.data = ResponseLoanStatus(**{"status_list": data})
                    Log.info(result.message)

            else:
                data = Loan.limit(limit).get().serialize()
                result.status = 200
                result.message = "Success Query Without Filter"
                result.data = ResponseLoanStatus(**{"status_list": data})
                Log.info(result.message)

        except ValidationError:
            m = 'Wrong data type!'
            Log.error(m)
            result.status = 400
            result.message = str(m)


        except Exception:
            m = "Error"
            Log.error(m)
            result.status = 400
            result.message = str(m)

        return result    

    @classmethod
    def read_loan_by_borrower(cls, cif):
        result = BaseResponse()
        result.status = 400

        if cif is not None:
            data = Borrower.where('cif',cif).get().serialize()
            result.status = 200
            result.message = "Success"
            result.data = data
        
        else:
            m = "cif not found!"
            Log.error(m)
            result.status = 404
            result.message = str(m)

        return result

    @classmethod
    def insert_data(cls, input_data=None):
        result = BaseResponse()
        result.status = 400

        try:
            if len(input_data.keys()) != 0:
                loan_id = str(int(Loan.max('loanid'))+1)
                input_data['loanid'] = loan_id
                Loan.insert(input_data)
                result.status = 200
                result.message = f"Success Input New Data with loanid : {loan_id}"
                Log.info(result.message)

            else:
                result.status = 400
                result.message = "There's no input data"
                Log.info(result.message)

        except:
            m = "Error"
            Log.error(m)
            result.status = 400
            result.message = str(m)

        return result

    @classmethod
    def delete_data(cls, loanid=None):
        result = BaseResponse()
        result.status = 400

        try:
            if loanid is not None and loanid in Loan.lists("loanid"):
                Loan.where('loanid', '=', loanid).delete()
                result.status = 200
                result.message = f"Success Delete data by loan id: {loanid}"
                Log.info(result.message)
            elif loanid is None:
                result.status = 400
                result.message = "There's no input"
                Log.info(result.message)
            else:
                result.status = 404
                result.message = "loan id not found"
                Log.info(result.message)
        except:
            m = "Error"
            Log.error(m)
            result.status = 400
            result.message = str(m)

        return result

    @classmethod
    def update_data(cls, loanid=None, update_data=None):
        result = BaseResponse()
        result.status = 400

        try:
            if loanid is not None and loanid in Loan.lists("loanid"):
                Loan.where('loanid', loanid).update(update_data)
                result.status = 200
                result.message = f"Update data by loan id: {loanid}"
                Log.info(result.message)
                
            else:
                result.status = 404
                result.message = "loan id not found"
        except:
            m = "Error"
            Log.error(m)
            result.status = 400
            result.message = str(m)

        return result


        


