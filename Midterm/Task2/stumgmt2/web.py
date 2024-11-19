#!/usr/bin/env python3
# 学生管理系统二代，分离了获取学生信息逻辑和输入输出逻辑
# 一代更比一代强

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
import uvicorn
from asyncio.queues import Queue as AsyncQueue
import asyncio

from stumgmt import StudentManagement
from models import *
from exc import *

logger = logging.getLogger('uvicorn')


async def process_transactions(app: FastAPI):
    while True:
        transaction = await app.state.transactions.get()
        logger.info(f"Processing transaction: {transaction}")
        if transaction.action == TransactionType.add:
            app.state.stumgmt.add_student(transaction.student)
        elif transaction.action == TransactionType.remove:
            app.state.stumgmt.remove_student_by_id(transaction.student.id)
        elif transaction.action == TransactionType.update:
            app.state.stumgmt.modify_information(
                transaction.student.id,
                transaction.student.name,
                transaction.student.college,
                transaction.student.gpa
            )


@asynccontextmanager
async def lifespan(app: FastAPI):
    # on_startup
    logger.info("欢迎使用先锋学生管理系统第二代")
    app.state.stumgmt = StudentManagement()
    app.state.transactions = AsyncQueue()
    asyncio.create_task(process_transactions(app))
    yield
    # on_shutdown
    logger.info('Saving data to disk')
    app.state.stumgmt.save_to_disk()

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/students")
async def query_students(
    query_by: Opt[OrderBy] = None,
    value: Opt[str] = '',
    order_by: Opt[OrderBy] = None,
    reverse: bool = False
) -> StudentQueryResponse:
    logger.info(f"Query students by {query_by} with value {value}")
    students = app.state.stumgmt.query_student(
        query_by, value, order_by, reverse)
    if not students:
        return StudentQueryResponse(code=404, message="未找到学生")
    return StudentQueryResponse(students=students)


@app.get("/student/count")
async def get_student_count() -> StudentCountResponse:
    return StudentCountResponse(count=app.state.stumgmt.count)


@app.put("/student/add")
async def add_student(student: Student) -> StudentResponse:
    logger.info(f"Add student: {student}")
    try:
        app.state.stumgmt.add_student(student)
        return StudentResponse(student=student)
    except StudentExistsError:
        logger.error("Student already exists")
        return StudentResponse(code=400, message="学生已存在")


@app.delete("/student/remove")
async def remove_student(student_id: int) -> BaseResponse:
    logger.info(f"Remove student by id: {student_id}")
    if app.state.stumgmt.remove_student_by_id(student_id):
        return BaseResponse(message="删除成功")
    else:
        logger.error("Student not found")
        return BaseResponse(code=404, message="学生不存在")


@app.patch("/student/update")
async def modify_student(
    student_id: int,
    name: Opt[str] = None,
    college: Opt[str] = None,
    gpa: Opt[float] = None
) -> StudentResponse:
    logger.info(f"Modify student by id: {student_id}")
    for attr in (name, college, gpa):
        if attr is not None:
            logger.info(f"Set {attr} to {name}")
    result: Student | bool = app.state.stumgmt.modify_information(
        student_id, name, college, gpa
    )
    if not result:
        logger.error("Student not found")
        return StudentResponse(code=404, message="学生不存在")
    return StudentResponse(student=result)


@app.post("/transactions/add")
async def add_transactions(transactions: list[Transaction]) -> BaseResponse:
    for transaction in transactions:
        app.state.transactions.put_nowait(transaction)
    return BaseResponse(message="添加成功")


@app.post("/save")
async def save_to_disk() -> BaseResponse:
    app.state.stumgmt.save_to_disk()
    return BaseResponse(message="保存成功")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
