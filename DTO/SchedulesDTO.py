class SchedulesDTO:
    def __init__(self, schedule_id, subject_id, class_id, teacher_id, title, day_of_week, start_time, end_time, room):
        self.schedule_id = schedule_id
        self.subject_id = subject_id
        self.class_id = class_id
        self.teacher_id = teacher_id
        self.title = title
        self.day_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time
        self.room = room
