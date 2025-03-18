class FaceRecognitionDTO:
    def __init__(self, face_id, student_id, image_url, embedding_data):
        self.face_id = face_id
        self.student_id = student_id
        self.image_url = image_url
        self.embedding_data = embedding_data
