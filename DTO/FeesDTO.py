class FeesDTO:
    def __init__(self, fee_id, student_id, amount, due_date, status):
        self.fee_id = fee_id
        self.student_id = student_id
        self.amount = amount
        self.due_date = due_date
        self.status = status
