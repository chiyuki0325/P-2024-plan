from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    college: str
    gpa: float

    def __str__(self):
        return f"学号: {self.id}, 姓名: {self.name}, 学院: {self.college}, 绩点: {self.gpa}"