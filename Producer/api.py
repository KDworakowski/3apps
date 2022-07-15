from doctest import Example
from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
from starlette.responses import HTMLResponse
from aio_pika import connect, Message
from typing import Dict
import json


from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
app = FastAPI()

successful_tasks = 0


class Task(BaseModel):
    taskid: str
    description: str
    params: Dict[str, str] = {}


@app.get("/")
async def read_root():
    return HTMLResponse(content = "POST /AddTasks<br />GET /GetStats")


async def send_rabbitmq(msg = {}):
    connection = await connect("amqp://guest:guest@localhost/")

    channel = await connection.channel()

    await channel.default_exchange.publish(
        Message(json.dumps(msg.dict()).encode("utf-8")),
        routing_key = "fastapi_task"
    )

    await connection.close()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

@app.post("/AddTasks")
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
    if not Task:
        raise HTTPException(status_code=400, detail="Bad request")
    global successful_tasks

    await send_rabbitmq(task)
    successful_tasks += 1

    return {"message": f"Task {task.taskid} added"}
