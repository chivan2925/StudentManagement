class AttendanceDTO:
    def __init__(self, attendance_id, face_id, schedule_id, attendance_date, status, image_url):
        self.attendance_id = attendance_id
        self.face_id = face_id
        self.schedule_id = schedule_id
        self.attendance_date = attendance_date
        self.status = status
        self.image_url = image_url
