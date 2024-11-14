#!/usr/bin/env python3
import unittest
from stumgmt import StudentManagement
from exc import *
from models import *

TEST_YAML_STRING= """
students:
  - name: "张三"
    id: 20240001
    college: "冶金学院"
    gpa: 3.8
  - name: "李四"
    id: 20240002
    college: "软件学院"
    gpa: 3.5
"""

class StudentMgmtTest(unittest.TestCase):
    def test_stu_init(self):
        stumgmt = StudentManagement(TEST_YAML_STRING)
        self.assertEqual(stumgmt.count, 2)
        self.assertEqual(stumgmt.student_list[0].name, "张三")
        self.assertEqual(stumgmt.student_list[1].college, "软件学院")
        self.assertFalse(stumgmt.student_list[1].gpa == 3.8)  # 李四的测试绩点是 3.5

    def test_stu_add(self):
        stumgmt = StudentManagement(TEST_YAML_STRING)
        stumgmt.add_student(Student(id=20240003, name="王五", college="计算机学院", gpa=3.9))
        self.assertEqual(stumgmt.count, 3)
        self.assertEqual(stumgmt.student_list[2].name, "王五")
        self.assertEqual(stumgmt.student_list[2].gpa, 3.9)
        with self.assertRaises(StudentExistsError):
            stumgmt.add_student(Student(id=20240003, name="王五", college="计算机学院", gpa=3.9))  # 重复添加

    def test_stu_del(self):
        stumgmt = StudentManagement(TEST_YAML_STRING)
        stumgmt.remove_student_by_id(20240001)
        self.assertEqual(stumgmt.count, 1)
        self.assertEqual(stumgmt.student_list[0].name, "李四")
        stumgmt = StudentManagement(TEST_YAML_STRING)
        stumgmt.remove_student_by_id(20240002)
        self.assertEqual(stumgmt.count, 1)
        self.assertEqual(stumgmt.student_list[0].name, "张三")
        self.assertFalse(stumgmt.remove_student_by_id(20240003))  # 王五不存在

    def test_stu_mod(self):
        stumgmt = StudentManagement(TEST_YAML_STRING)
        stumgmt.modify_information(20240001, college="计算机学院", gpa=4.0)
        # 哥们转专业了，绩点 4.0
        self.assertEqual(stumgmt.student_list[0].college, "计算机学院")
        self.assertEqual(stumgmt.student_list[0].gpa, 4.0)

    def test_stu_sel(self):
        stumgmt = StudentManagement(TEST_YAML_STRING)
        self.assertEqual(stumgmt.query_student(OrderBy.id, "20240001"), [stumgmt.student_list[0]])

    def test_stu_sort(self):
        stumgmt = StudentManagement(TEST_YAML_STRING)
        sorted_list = stumgmt.query_student(None, '', OrderBy.gpa, False)
        self.assertEqual(sorted_list[0].name, "李四")
        self.assertEqual(sorted_list[1].name, "张三")

if __name__ == '__main__':
    unittest.main()