import yaml
from typing import Optional as Opt

from models import *
from exc import *

STU_FILE = "students.yml"  # 默认路径


class StudentManagement:
    def __init__(self, yaml_string: Opt[str] = None):
        self.student_list = []

        if yaml_string is None:
            with open(STU_FILE, "r") as f:
                yaml_string = f.read()

        student_list = yaml.safe_load(yaml_string)['students']
        self.student_list = [Student.model_validate(
            student) for student in student_list]

    @property
    def count(self):
        return len(self.student_list)

    def add_student(self, student: Student):
        for s in self.student_list:
            if s.id == student.id:
                raise StudentExistsError
        self.student_list.append(student)

    def query_student(
            self,
            query_by: Opt[OrderBy],
            value: str,
            order_by: Opt[OrderBy] = None,
            reverse: bool = False
    ) -> list[Student]:
        if query_by is not None:
            if query_by == OrderBy.id:
                result = [s for s in self.student_list if s.id == int(value)]
            elif query_by == OrderBy.gpa:
                result = [
                    s for s in self.student_list if s.gpa == float(value)]
            else:
                result = [
                    s for s in self.student_list
                    if getattr(s, query_by.value) == value
                ]
        else:
            result = self.student_list
        if order_by is None:
            return result
        return sorted(result, key=lambda x: getattr(x, order_by.value), reverse=reverse)

    def remove_student_by_id(self, student_id: int) -> bool:
        student_list = [s for s in self.student_list if s.id != student_id]
        if len(student_list) == len(self.student_list):
            return False
        self.student_list = student_list
        return True

    def modify_information(
            self,
            student_id: int,
            name: Opt[str] = None,
            college: Opt[str] = None,
            gpa: Opt[float] = None
    ) -> Student | bool:
        for student in self.student_list:
            if student.id == student_id:
                if name is not None:
                    student.name = name
                if college is not None:
                    student.college = college
                if gpa is not None:
                    student.gpa = gpa
                return student
        return False

    def save_to_disk(self):
        with open(STU_FILE, "w") as f:
            yaml.dump({"students": self.student_list}, f)
