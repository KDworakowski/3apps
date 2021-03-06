from fastapi import FastAPI, Body
from pydantic import BaseModel
from starlette.responses import HTMLResponse
from typing import Dict
import json
import os

import pika

from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
app = FastAPI()

successful_tasks = 0
credentials = pika.PlainCredentials(os.getenv("RABBITMQ_USER", "guest"), os.getenv("RABBITMQ_PASSWORD", "guest"))
connection = pika.BlockingConnection(pika.ConnectionParameters(host=(os.getenv("RABBITMQ_HOST", "localhost")),credentials=credentials))
channel = connection.channel()
class Task(BaseModel):
    taskid: str
    description: str
    params: Dict[str, str] = {}


@app.get("/")
async def read_root():
    return HTMLResponse(content = "POST /AddTasks<br />GET /GetStats")


def send_rabbitmq(msg = {}):
    channel.basic_publish(exchange='', routing_key=os.getenv("RABBIT_ROUTING", "fastapi_task"), body=json.dumps(msg.dict()).encode("utf-8"))

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

@app.post("/add")
async def add_tasks(
    task: Task = Body(
        ...,
        example = {
            "taskid": "task1234",
            "description": "Example description",
            "params": {
                "test1": "1234",
                "test2": "5678"
            }
        }
    )
):
    global successful_tasks

    send_rabbitmq(task)
    successful_tasks += 1

    return {"message": f"Task {task.taskid} added"}

@app.on_event("shutdown")
def stop_connection():
    connection.close()
