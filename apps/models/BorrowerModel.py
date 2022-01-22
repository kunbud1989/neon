from apps.models import Model
from orator.orm import has_many
from apps.models.LoanDataModel import Loan

class Borrower(Model):
    __table__ = "borrower"
    __primary_key__ = 'cif'

    @has_many(foreign_key='cif')
    def loans(self):
        return Loan





