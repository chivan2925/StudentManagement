class CourseMaterialsDTO:
    def __init__(self, material_id, subject_id, teacher_id, title, description, upload_date, file_url):
        self.material_id = material_id
        self.subject_id = subject_id
        self.teacher_id = teacher_id
        self.title = title
        self.description = description
        self.upload_date = upload_date
        self.file_url = file_url
