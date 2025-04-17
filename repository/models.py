from pydantic import BaseModel
from datetime import datetime

class Faculty(BaseModel):
    name: str
    department: str
    email_id: str
    photo_id: str
    created: int = int(datetime.timestamp(datetime.now()))
    updated: int = int(datetime.timestamp(datetime.now()))
    

class Course(BaseModel):
    name: str
    offering_department: str
    course_code: str
    barred_departments: str
    created: int = int(datetime.timestamp(datetime.now()))
    updated: int = int(datetime.timestamp(datetime.now()))

class Quiz(BaseModel):
    course_id: int
    taken_on: int = int(datetime.timestamp(datetime.now()))
    duration: int
    form_link = str