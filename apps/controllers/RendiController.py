from apps.helper import Log
from apps.schemas import BaseResponse
from apps.schemas.SchemaCIF import RequestLoanStatus, ResponseLoanStatus
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
from apps.models.LoanModel import Loan

SALT = PARAMS.SALT.salt


class ControllerRendi(object):
    @classmethod
    def get_active_borrower_from_type_and_status_by_rendi(cls, input_data=None):
        input_data = RequestLoanStatus(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.limit is None:
                input_data.limit = Loan.count('loanid')

            if (input_data.loan_status is not None) and (input_data.loan_type is not None):

                if input_data.loan_status not in range (Loan.min('loan_status'), Loan.max('loan_status')+1): 
                    result.message = f"No loan status above {Loan.max('loan_status')} or below {Loan.min('loan_status')}"
                    Log.info(result.message)

                elif input_data.loan_type not in range (Loan.min('loan_type'), Loan.max('loan_type')+1):
                    result.message = f"No loan type above {Loan.max('loan_type')} or below {Loan.min('loan_type')}"
                    Log.info(result.message)

                else:
                    data = Loan.where('loan_status', '=', input_data.loan_status).where('loan_type', '=', input_data.loan_type).limit(input_data.limit).get().serialize()
                    result.status = 200
                    result.message = "Success"
                    result.data = ResponseLoanStatus(**{"status_list": data})
                    Log.info(result.message)

            elif input_data.loan_status is not None:
                if input_data.loan_status not in range (Loan.min('loan_status'), Loan.max('loan_status')+1): 
                    result.message = f"No loan status above {Loan.max('loan_status')} or below {Loan.min('loan_status')}"
                    Log.info(result.message)

                else:
                    data = Loan.where('loan_status', '=', input_data.loan_status).limit(input_data.limit).get().serialize()
                    result.status = 200
                    result.message = "Success"
                    result.data = ResponseLoanStatus(**{"status_list": data})
                    Log.info(result.message)

            elif input_data.loan_type is not None:
                if input_data.loan_type not in range (Loan.min('loan_type'), Loan.max('loan_type')+1):
                    result.message = f"No loan type above {Loan.max('loan_type')} or below {Loan.min('loan_type')}"
                    Log.info(result.message)

                else:
                    data = Loan.where('loan_type', '=', input_data.loan_type).limit(input_data.limit).get().serialize()
                    result.status = 200
                    result.message = "Success"
                    result.data = ResponseLoanStatus(**{"status_list": data})
                    Log.info(result.message)

            else:
                data = Loan.limit(input_data.limit).get().serialize()
                result.status = 200
                result.message = "Success Query Without Filter"
                result.data = ResponseLoanStatus(**{"status_list": data})
                Log.info(result.message)


        except Exception:
            m = "Error"
            Log.error(m)
            result.status = 400
            result.message = str(m)

        return result
