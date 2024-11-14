#!/usr/bin/env python3
import unittest
import main as stumgmt

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
        stumgmt.stu_init(TEST_YAML_STRING)
        self.assertEqual(len(stumgmt.stu_list), 2)
        self.assertEqual(stumgmt.stu_list[0].name, "张三")
        self.assertEqual(stumgmt.stu_list[1].college, "软件学院")
        self.assertFalse(stumgmt.stu_list[1].gpa == 3.8)  # 李四的测试绩点是 3.5

    def test_get_choice(self):
        self.assertEqual(stumgmt.get_choice(1), stumgmt.CHOICES.ADD)
        self.assertEqual(stumgmt.get_choice(6), stumgmt.CHOICES.SAVE)
        self.assertEqual(stumgmt.get_choice(0), stumgmt.CHOICES.EXIT)
        with self.assertRaises(ValueError):
            stumgmt.get_choice(7)

    def test_stu_add(self):
        stumgmt.stu_init(TEST_YAML_STRING)
        stumgmt.stu_add(stumgmt.Student(id=20240003, name="王五", college="计算机学院", gpa=3.9), False)
        self.assertEqual(len(stumgmt.stu_list), 3)
        self.assertEqual(stumgmt.stu_list[2].name, "王五")
        self.assertEqual(stumgmt.stu_list[2].gpa, 3.9)
        self.assertFalse(stumgmt.stu_add(stumgmt.Student(id=20240003, name="王五", college="计算机学院", gpa=3.9), False))  # 重复添加

    def test_stu_del(self):
        stumgmt.stu_init(TEST_YAML_STRING)
        stumgmt.stu_del("20240001")
        self.assertEqual(len(stumgmt.stu_list), 1)
        self.assertEqual(stumgmt.stu_list[0].name, "李四")
        stumgmt.stu_init(TEST_YAML_STRING)
        stumgmt.stu_del("李四")
        self.assertEqual(len(stumgmt.stu_list), 1)
        self.assertEqual(stumgmt.stu_list[0].name, "张三")
        self.assertFalse(stumgmt.stu_del("王五"))  # 王五不存在

    def test_stu_mod(self):
        stumgmt.stu_init(TEST_YAML_STRING)
        stumgmt.stu_mod("20240001", stumgmt.Student(id=20240001, name="张三", college="计算机学院", gpa=4.0))
        # 哥们转专业了，绩点 4.0
        self.assertEqual(stumgmt.stu_list[0].college, "计算机学院")
        self.assertEqual(stumgmt.stu_list[0].gpa, 4.0)
        self.assertFalse(stumgmt.stu_mod("李四", stumgmt.Student(id=20240001, name="张三", college="计算机学院", gpa=4.0)))

    def test_stu_sel(self):
        stumgmt.stu_init(TEST_YAML_STRING)
        self.assertEqual(stumgmt.stu_sel("20240001"), "学号: 20240001, 姓名: 张三, 学院: 冶金学院, 绩点: 3.8")
        self.assertEqual(stumgmt.stu_sel("李四"), "学号: 20240002, 姓名: 李四, 学院: 软件学院, 绩点: 3.5")

    def test_stu_sort(self):
        stumgmt.stu_init(TEST_YAML_STRING)
        stumgmt.stu_sort("gpa", False)  # 公开处刑
        self.assertEqual(stumgmt.stu_list[0].name, "李四")
        self.assertEqual(stumgmt.stu_list[1].name, "张三")

if __name__ == '__main__':
    unittest.main()