from apps.models import Model


class Loan(Model):
    __table__ = 'neon_dataset'
    __primary_key__ = 'loanid'
