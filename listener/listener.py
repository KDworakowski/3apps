#!/usr/bin/env python

import asyncio
from aio_pika import connect, IncomingMessage
import json
import pymongo
import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient.database_sample
my_collection = db["database"]

async def on_message(message: IncomingMessage):
    txt = message.body.decode("utf-8")

    data = json.loads(txt)
    timestamp = datetime.datetime.utcnow()
    my_collection.create_index("date", expireAfterSeconds=60)
    my_collection.insert_one(data | {"date": timestamp})

    print(json.loads(txt))


async def main(loop):


    connection = await connect("amqp://guest:guest@localhost/", loop = loop)

    channel = await connection.channel()

    queue = await channel.declare_queue("fastapi_task")

    await queue.consume(on_message, no_ack = True)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    loop.run_forever()
