#import statements
from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studendEntity, listOfStudentEntity
from bson import ObjectId

student_router = APIRouter()

#getting all studends Route
@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntity(connection.local.student.find())

#get one student with matching id
@student_router.get('/students/{studentId}')
async def find_student_by_id(studentId):
    return studendEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

#creating a student
@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())

#update a student
@student_router.put('/students/{studentId}')
async def update_student(studentId, student: Student):
    #finde the student and than update it with new student data
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(studentId)},
        {"$set": dict(student)}
    )
    return studendEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

#delete a student
@student_router.delete('/studens/{studenId}')
async def delete_student(studentId):
    #find the student and delete it and also return the same student object
    return studendEntity(connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)}))
