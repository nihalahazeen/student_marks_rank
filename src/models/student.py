from typing import Optional, Any, Union

from beanie import Document
from pydantic import BaseModel


class Student(Document):
    student_name: str
    student_id: Union[str, None] = None
    subject: str
    marks: int


    class Config:
        schema_extra = {
            "example": {
                "student_id":"hash(student_name)",
                "student_name": "Alice",
                "subject":"Maths",
                "marks": 34
            }
        }


class UpdateStudentModel(BaseModel):
    student_id: Optional[str]
    student_name: Optional[str]
    subject: Optional[str]
    marks: Optional[int]

    class Collection:
        name = "student"

    class Config:
        schema_extra = {
            "example": {
                "student_id":"hash(student_name)",
                "student_name": "Alice",
                "subject":"Maths",
                "marks": 34
            }
        }


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data"
            }
        }
