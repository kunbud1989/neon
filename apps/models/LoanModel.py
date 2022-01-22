from apps.models import Model


class Loan(Model):
    __table__ = 'pandas_neon_dataset1'
    __primary_key__ = 'loanid'
    __timestamps__ = False
