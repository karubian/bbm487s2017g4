import datetime


class Loan:
    def __init__(self, user, book):
        self.book_id = book
        self.user_id = user
        self.startDate = datetime.datetime.now() - datetime.timedelta(days=50)
        # self.startDate = datetime.datetime.now()
        self.returnDate = self.startDate + datetime.timedelta(days=40)
        self.currentFine = 0
        self.status = 0

    def calculate_fine(self, elapsed_days):
        self.currentFine = 5 + (elapsed_days - 40) * 1.5

    def check_status(self):
        elapsed_time = datetime.datetime.now() - self.startDate
        elapsed_days = divmod(elapsed_time.total_seconds(), 3600 * 24)[0]
        if elapsed_days > 40:
            self.calculate_fine(elapsed_days)
            self.status = 1
        else:
            self.status = 0
