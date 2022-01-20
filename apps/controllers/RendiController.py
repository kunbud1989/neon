from cmath import log
from pydantic import ValidationError
from turtle import update
from apps.helper import Log
from apps.schemas import BaseResponse
from apps.schemas.SchemaRendi import ResponseLoanStatus, RequestInsertData, RequestUpdateData
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
from apps.models.LoanModel import Loan

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
    def insert_data_by_loanid(cls, input_data=None):
        input_data = RequestInsertData(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.loanid is not None:
                Loan.insert(input_data)
                data = Loan.where('loanid', '=', input_data.loanid).get().serialize()
                result.status = 200
                result.message = "Success Input New Data"
                result.data = ResponseLoanStatus(**{'status_list': data})
                Log.info(result.message)
            else:
                result.status = 404
                result.message = "We can't insert your data because loanid parameter is empty"
                Log.info(result.message)

        except:
            m = "Error"
            Log.error(m)
            result.status = 400
            result.message = str(m)

        return result

    @classmethod
    def delete_data_by_idno(cls, id_no=None):
        result = BaseResponse()
        result.status = 400

        try:
            if id_no is not None:
                if id_no in Loan.lists("idno"):
                    data = Loan.where('idno', '=', id_no)
                    view = data.get().serialize()
                    data.delete()
                    result.status = 200
                    result.message = f"Success Delete data by id no: {id_no}"
                    result.data = ResponseLoanStatus(**{'status_list': view})
                    Log.info(result.message)
                else:
                    result.status = 404
                    result.message = "idno not found"
            else:
                result.status = 400
                result.message = "There's no input"
                Log.info(result.message)
        except:
            m = "Error"
            Log.error(m)
            result.status = 400
            result.message = str(m)

        return result

    @classmethod
    def update_demography_data(cls, id_no=None, update_data=None):
        update_data = RequestUpdateData(**update_data)
        result = BaseResponse()
        result.status = 400

        try:
            if id_no is not None:
                if id_no in Loan.lists("idno"):
                    Loan.where('idno', id_no).update(update_data)
                    data = Loan.where('idno', id_no).get().serialize()
                    result.status = 200
                    result.message = f"Update phone number by id no: {id_no}"
                    result.data = ResponseLoanStatus(**{'status_list': data})
                    Log.info(result.message)
                else:
                    result.status = 404
                    result.message = "idno not found"
            else:
                result.status = 400
                result.message = "There's no input"
                Log.info(result.message)
        except:
            m = "Error"
            Log.error(m)
            result.status = 400
            result.message = str(m)

        return result


        


