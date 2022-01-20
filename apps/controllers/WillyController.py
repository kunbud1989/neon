from apps.helper import Log
from apps.schemas import BaseResponse
from apps.helper.ConfigHelper import encoder_app
from apps.schemas.SchemaLoanid import RequestMyLoan, ResponseMyLoan
from apps.schemas.SchemaRiskyUser import RequestRiskyUser, ResponseRiskyUser
from main import PARAMS
from apps.models.LoanModel import Loan

SALT = PARAMS.SALT.salt


class ControllerWilly(object):
    @classmethod
    def get_user_by_loanid(cls, input_data=None):
        input_data = RequestMyLoan(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.loanid is not None:
                if input_data.loanid in Loan.lists("loanid"):
                    data = Loan.where('loanid', '=', input_data.loanid).get().serialize()
                    result.status = 200
                    result.message = "Success"
                    result.data = ResponseMyLoan(**{"loanid_list": data})
                    Log.info(result.message)
                else:
                    e = "loanid not found!"
                    Log.error(e)
                    result.status = 404
                    result.message = str(e)
            else:
                e = "no loanid params found!"
                Log.error(e)
                result.status = 404
                result.message = str(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def get_risky_user(cls, risky):
        result = BaseResponse()
        result.status = 400

        try:
            if risky is not None:
                if risky in Loan.lists("risky"):
                    data = Loan.where('risky', '=', risky).get().serialize()
                    result.status = 200
                    result.message = "Success"
                    result.data = ResponseRiskyUser(**{"risky_list": data})
                    Log.info(result.message)
                elif risky not in range (Loan.min('risky'), Loan.max('risky')+1):
                    result.status = 404
                    result.message = f"No loan status above {Loan.max('risky')} or below {Loan.min('risky')}" 
                else:
                    result.status = 404
                    result.message = "not found"

        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

