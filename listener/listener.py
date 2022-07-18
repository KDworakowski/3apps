#!/usr/bin/env python

import asyncio
from aio_pika import connect, IncomingMessage
import json
import pymongo
import datetime

MONGODB_URL="mongodb://localhost:27017/"
RABBITMQ_URL="amqp://guest:guest@localhost/"
RABBIT_ROUTING="fastapi_task"

myclient = pymongo.MongoClient(MONGODB_URL)
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


    connection = await connect(RABBITMQ_URL, loop = loop)

    channel = await connection.channel()

    queue = await channel.declare_queue(RABBIT_ROUTING)

    await queue.consume(on_message, no_ack = True)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    loop.run_forever()
