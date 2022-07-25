#! uvicorn api:app --reload
# uvicorn main:app --host 0.0.0.0 --port 80
# hypercorn main:app --bind 0.0.0.0:80
from fastapi import FastAPI
import pymongo
import os

app = FastAPI()

# Create a connection to MongoDB and create DB

myclient = pymongo.MongoClient(os.getenv("MONGODB_URL", "mongodb://localhost:27017/"))
db = myclient.database_sample
my_collection = db["database"]

@app.get("/size")
def get_stats():

    # Count number of documents in database
    numberOfDocs = my_collection.count_documents({})
    return {"message": f"Total objects {numberOfDocs}"}
