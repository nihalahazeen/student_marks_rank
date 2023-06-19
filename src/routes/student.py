from fastapi import APIRouter, Body

from src.database.database import *
from src.models.student import *
from src.helpers.id_generator import generate_hash

router = APIRouter()


@router.get("/", response_description="Students retrieved", response_model=Response)
async def get_students():
    students = await retrieve_students()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Students data retrieved successfully",
        "data": students
    }


@router.get("/{id}", response_description="Student data retrieved", response_model=Response)
async def get_student_data(id: PydanticObjectId):
    student = await retrieve_student(id)
    if student:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Student data retrieved successfully",
            "data": student
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Student doesn't exist",
    }


@router.post("/", response_description="Student data added into the database", response_model=Response)
async def add_student_data(student: Student = Body(...)):
    if not student:
        return {
        "status_code": 422,
        "response_type": "error",
        "description": "Please Provide input"
    }
    student.student_id = generate_hash(student.student_name)
    find_student = await retrieve_student_sub(student.student_id, student.subject)
    if find_student:
        return {
        "status_code": 400,
        "response_type": "error",
        "description": "Student already exists",
        "data": f"Document id {find_student}"
    }
    new_student = await add_student(student)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Student created successfully",
        "data": new_student
    }


@router.delete("/{id}", response_description="Student data deleted from the database")
async def delete_student_data(id: PydanticObjectId):
    deleted_student = await delete_student(id)
    if deleted_student:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Student marks with ID: {} removed".format(id),
            "data": deleted_student
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Student marks with id {0} doesn't exist".format(id),
        "data": False
    }


@router.put("/{id}", response_model=Response)
async def update_student(id: PydanticObjectId, req: UpdateStudentModel = Body(...)):
    updated_student = await update_student_data(id, req.dict())
    if updated_student:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Student marks with ID: {} updated".format(id),
            "data": updated_student
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Student marks with ID: {} not found".format(id),
        "data": False
    }
