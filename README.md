# ServerCode
Singelton
from pymongo import MongoClient

class BaseModel:
    _connection = None

    @classmethod
    def get_connection(cls):
        if not cls._connection:
            # Replace the connection URL with your Atlas MongoDB connection URL
            cls._connection = MongoClient('<connection_url>')
        return cls._connection

    def __init__(self):
        self.db = self.get_connection().my_database
        # You can add other initialization logic here

    # You can define other common methods or properties for your models here

class StudentModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.collection = self.db.students

    # Add specific methods or properties for the student model here

class TeacherModel(BaseModel):
    def __init__(self):
        super().__init__()
        self.collection = self.db.teachers

    # Add specific methods or properties for the teacher model here
