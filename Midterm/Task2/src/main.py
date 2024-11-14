#!/usr/bin/env python3
# 学生管理系统
# PS: 可以仅以 “姓名” / “学号” 来代指学生信息

from enum import Enum
import sys
import os
import yaml

from models import Student
from typing import List, Dict, Callable


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


STU_FILE = "students.yml"

MENU: Dict[CHOICES, str] = {
    CHOICES.ADD: "添加学生",
    CHOICES.DEL: "删除学生",
    CHOICES.MOD: "修改信息",
    CHOICES.SEL: "查询学生",
    CHOICES.SORT: "索引全部学生",
    CHOICES.SAVE: "保存信息",
    CHOICES.EXIT: "退出"
}

stu_list: List[Student] = []


def stu_init(yaml_string: str = None):
    """此函数用于, 从文件中, 初始化学生信息"""

    global stu_list

    if yaml_string:
        student_list: str = yaml.safe_load(yaml_string)['students']
    else:
        with open(STU_FILE, "r") as f:
            student_list: str = yaml.safe_load(f)['students']
    stu_list = [Student.model_validate(student) for student in student_list]


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

    print("--- 先锋学生管理系统 ---")
    print(f"当前学生人数: {len(stu_list)}")
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


def stu_add(stu: Student = None, continue_add: bool = True):
    """此函数用于, 添加学生信息"""

    if not stu:
        print('请输入学生信息:')
        stu = input_student()
    
    for student in stu_list:
        if student.id == stu.id or student.name == stu.name:
            print('学生已存在。')
            return False
    stu_list.append(stu)
    print(f'添加成功: {stu}')

    if continue_add and input("是否继续添加学生信息? (y/n): ").lower() == "y":
        stu_add(continue_add=True)


def stu_del(query: str = None):
    """此函数用于, 删除学生信息"""

    global stu_list
    if not query:
        query: str = input('输入要删除的学生的学号或姓名: ')

    # 使用 Python 的列表推导式以简化代码
    if query.isdigit():
        stu_list = [
            stu for stu in stu_list if
            stu.id != int(query)
        ]
    else:
        stu_list = [
            stu for stu in stu_list if
            stu.name != query
        ]
    print('删除成功。')


def stu_mod(query: str = None, new_stu: Student = None):
    """此函数用于, 修改学生信息"""

    if not query:
        query: str = input('输入要修改的学生的学号或姓名: ')
    idx: int = -1

    # 找到要修改的学生
    for i, stu in enumerate(stu_list):
        if query.isdigit() and stu.id == int(query) or stu.name == query:
            idx = i
            break

    if idx == -1:
        print('未找到该学生。')
        return  # 不使用 else，提前返回以减少缩进

    if not new_stu:
        print('请输入新的学生信息:')
        new_stu = input_student()
    
    if new_stu.id != stu_list[idx].id and new_stu.name != stu_list[idx].name:
        for student in stu_list:
            if student.id == new_stu.id or student.name == new_stu.name:
                print('学生已存在。')
                return False

    stu_list[idx] = new_stu
    print(f'修改成功: {new_stu}')


def stu_sel(query: str = None):
    """此函数用于, 查询学生信息"""

    if not query:
        query: str = input('输入要查询的学生的学号或姓名: ')

    for stu in stu_list:
        if query.isdigit() and stu.id == int(query) or stu.name == query:
            print(stu)
            return str(stu)  # 用于进行测试

    print('未找到该学生！')


def stu_sort(order_by: str = None, reverse: bool = None):
    """此函数用于, 索引全部学生信息"""

    if not order_by:
        order_by: str = input('输入排序依据 (id, name, college, gpa): ') or 'id'
    if reverse is None:
        reverse: bool = input('是否逆序 (y/n): ').lower() == 'n'

    # getattr 类似 JavaScript 的中括号，可以通过字符串获取对象的属性
    stu_list.sort(key=lambda stu: getattr(stu, order_by), reverse=reverse)

    for stu in stu_list:
        print(stu)


def stu_save():
    """此函数用于, 将学生信息保存到文件中"""

    with open(STU_FILE, "w") as f:
        yaml.dump({"students": [stu.model_dump() for stu in stu_list]}, f)
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
    stu_init()
    main()
