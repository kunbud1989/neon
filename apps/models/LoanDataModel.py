from apps.models import Model
from orator.orm import belongs_to


class Loan(Model):
    __table__ = "loan"
    __primary_key__ = 'loanid'