#!/usr/bin/env python3
# 学生管理系统二代，分离了获取学生信息逻辑和输入输出逻辑
# 一代更比一代强

from enum import Enum
import sys
import os
from typing import List, Dict, Callable
import yaml

from stumgmt import StudentManagement
from models import *
from exc import *


stumgmt = StudentManagement()


class CHOICES(Enum):
    """此类用于, 定义用户输入的选项"""
    ADD = 1
    DEL = 2
    MOD = 3
    SEL = 4
    SORT = 5
    SAVE = 6
    EXIT = 0
    UNKNOWN = -1


MENU: Dict[CHOICES, str] = {
    CHOICES.ADD: "添加学生",
    CHOICES.DEL: "删除学生",
    CHOICES.MOD: "修改信息",
    CHOICES.SEL: "查询学生",
    CHOICES.SORT: "索引全部学生",
    CHOICES.SAVE: "保存信息",
    CHOICES.EXIT: "退出"
}


def get_choice(i: int = None) -> CHOICES:
    """此函数用于, 在命令行里, 获取用户输入的选项"""

    if i is not None:
        return CHOICES(i)

    try:
        return CHOICES(int(input("请输入选项: ")))
    except ValueError:
        print("输入有误, 请重新输入")
        return get_choice()


def menu():
    """此函数用于, 在命令行里, 打印出菜单"""

    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

    print("--- 先锋学生管理系统第二代 ---")
    print(f"当前学生人数: {stumgmt.count}")
    for choice, desc in MENU.items():
        print(f"{choice.value}: {desc}")


def input_student() -> Student:
    """输入学生信息"""
    return Student.model_validate({
        "id": int(input("学号: ")),
        "name": input("姓名: "),
        "college": input("学院: "),
        "gpa": float(input("绩点: "))
    })


def stu_add(stu):
    """此函数用于, 添加学生信息"""

    print('请输入学生信息:')
    stu = input_student()

    try:
        stumgmt.add_student(stu)
    except StudentExistsError:
        print('学生已存在。')
        return False

    print('添加成功:', stu)

    if input("是否继续添加学生信息? (y/n): ").lower() == "y":
        stu_add()


def stu_del():
    """此函数用于, 删除学生信息"""

    student_id: int = int(input('输入要删除的学生的学号: '))
    if stumgmt.remove_student_by_id(student_id):
        print('删除成功。')
    else:
        print('未找到该学生。')


def stu_mod():
    """此函数用于, 修改学生信息"""

    student_id_query: str = input('输入要修改信息的学生的学号: ')

    stu: List[Student] = stumgmt.query_student(OrderBy.id, student_id_query)

    if not stu:
        print('未找到该学生。')
        return

    stu = stu[0]
    print('当前信息:', stu)

    name: str = input('姓名: ') or stu.name
    college: str = input('学院: ') or stu.college
    gpa: float = float(input('绩点: ')) or stu.gpa

    result = stumgmt.modify_information(stu.id, name, college, gpa)

    print('修改成功:', result)


def stu_sel():
    """此函数用于, 查询学生信息"""
    
    query_by: OrderBy = OrderBy(
        input('输入查询依据 (id, name, college, gpa): ') or 'id'
    )
    value: str = input('输入查询值: ')

    result = stumgmt.query_student(query_by, value)

    if not result:
        print('未找到学生。')
        return

    for stu in result:
        print(stu)


def stu_sort():
    """此函数用于, 索引全部学生信息"""
    
    order_by: OrderBy = OrderBy(
        input('输入排序依据 (id, name, college, gpa): ') or 'id'
    )
    reverse: bool = input('是否逆序? (y/n): ').lower() == 'y'

    result = stumgmt.query_student(None, '', order_by, reverse)

    for stu in result:
        print(stu)



def stu_save():
    """此函数用于, 将学生信息保存到文件中"""
    stumgmt.save_to_disk()
    print('保存成功。')


FUNCTIONS: Dict[CHOICES, Callable] = {
    CHOICES.ADD: stu_add,
    CHOICES.DEL: stu_del,
    CHOICES.MOD: stu_mod,
    CHOICES.SEL: stu_sel,
    CHOICES.SORT: stu_sort,
    CHOICES.SAVE: stu_save,
    CHOICES.EXIT: exit
}


def exec(choice: CHOICES):
    """此函数用于, 根据用户输入的选项, 执行相应的功能"""
    FUNCTIONS[choice]()


def main():
    """尽量不要修改此函数的代码, 此函数用于全局调用"""
    user_choice = CHOICES(-1)
    while user_choice.value != 0:
        menu()
        user_choice = get_choice()
        exec(user_choice)
        input("按 Enter 键继续...")
    pass


if __name__ == '__main__':
    main()
