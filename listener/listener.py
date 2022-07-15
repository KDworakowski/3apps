#!/usr/bin/env python

import asyncio
from aio_pika import connect, IncomingMessage
import json
import pymongo


async def on_message(message: IncomingMessage):
    myclient = pymongo.MongoClient("mongodb://host.docker.internal:27017/")
    db = myclient.database_sample
    my_collection = db["database"]

    txt = message.body.decode("utf-8")

    data = json.loads(txt)
    my_collection.insert_one(data)

    print(json.loads(txt))


async def main(loop):


    connection = await connect("amqp://guest:guest@host.docker.internal/", loop = loop)

    channel = await connection.channel()

    queue = await channel.declare_queue("fastapi_task")

    await queue.consume(on_message, no_ack = True)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    loop.run_forever()
