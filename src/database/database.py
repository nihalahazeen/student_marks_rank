from typing import List, Union

from beanie import PydanticObjectId

from src.models.student import Student

student_collection = Student


async def retrieve_students() -> List[Student]:
    students = await student_collection.all().to_list()
    return students


async def add_student(new_student: Student) -> Student:
    student = await new_student.create()
    return student


async def retrieve_student(id: PydanticObjectId) -> Student:
    student = await student_collection.get(id)
    if student:
        return student


async def delete_student(id: PydanticObjectId) -> bool:
    student = await student_collection.get(id)
    if student:
        await student.delete()
        return True


async def update_student_data(id: PydanticObjectId, data: dict) -> Union[bool, Student]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in des_body.items()
    }}
    student = await student_collection.get(id)
    if student:
        await student.update(update_query)
        return student
    return False


async def retrieve_student_sub(student_id: str, subject: str):
    student = await student_collection.find_one(Student.student_id == student_id, Student.subject == subject)
    if student:
        return student.id
    else:
        return None


async def calculate_rank():
    pipeline = [
        { "$group": { "_id": "$student_id", "average_mark": {"$avg": "$marks"}, "student_name": {"$first": "$student_name" } } },
        { "$sort": {"average_mark": -1} },
        { "$group": { "_id": None, "students": { "$push": { "student_id": "$_id", "average_mark": "$average_mark", "student_name": "$student_name" } } } },
    ]
    rank = await student_collection.aggregate(pipeline).to_list(length=None)
    return rank
