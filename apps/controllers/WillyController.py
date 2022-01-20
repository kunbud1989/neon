from apps.helper import Log
from apps.schemas import BaseResponse
from apps.helper.ConfigHelper import encoder_app
from apps.schemas.SchemaLoanid import RequestMyLoan, ResponseMyLoan
from main import PARAMS
from apps.models.LoanModel import Loan

SALT = PARAMS.SALT.salt


class ControllerWilly(object):
    @classmethod
    def get_user_by_loanid(cls, input_data=None):
        input_data = RequestMyLoan(**input_data)
        result = BaseResponse()
        result.status = 400
        # temp = Loan.where('loanid', '=', input_data.loanid).get().serialize()
        # print(type(temp))

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