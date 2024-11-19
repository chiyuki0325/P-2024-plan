from pydantic import BaseModel
from typing import Optional as Opt
from enum import Enum

class Student(BaseModel):
    id: int
    name: str
    college: str
    gpa: float

    def __str__(self):
        return f"学号: {self.id}, 姓名: {self.name}, 学院: {self.college}, 绩点: {self.gpa}"


class OrderBy(str, Enum):
    id = "id"
    name = "name"
    college = "college"
    gpa = "gpa"


class BaseResponse(BaseModel):
    code: Opt[int] = 200
    message: Opt[str] = "OK"


class StudentCountResponse(BaseResponse):
    count: int


class StudentResponse(BaseResponse):
    student: Opt[Student] = None


class StudentQueryResponse(BaseResponse):
    students: list[Student]

class TransactionType(str, Enum):
    add = "add"
    remove = "remove"
    update = "update"

class Transaction(BaseModel):
    type: TransactionType
    student: Opt[Student] = None
    student_id: Opt[int] = None
    name: Opt[str] = None
    college: Opt[str] = None
    gpa: Opt[float] = None
