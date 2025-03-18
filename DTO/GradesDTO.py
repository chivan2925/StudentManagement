class GradesDTO:
    def __init__(self, grade_id, enrollment_id, midterm, final, total):
        self.grade_id = grade_id
        self.enrollment_id = enrollment_id
        self.midterm = midterm
        self.final = final
        self.total = total