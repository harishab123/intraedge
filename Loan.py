from datetime import datetime

class Loan:
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.loan_date = datetime.now()
        self.return_date = None

    def mark_returned(self):
        self.return_date = datetime.now()
