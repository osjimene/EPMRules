import os
import pymongo
from pymongo import MongoClient


connectionString = os.getenv("Connection_String")
appinfo = MongoClient(connectionString)

db = appinfo["appinfo"]
collection = db["appinfo"]


#insert data into the database
def insert_data(data: dict):
    collection.insert_one(data)


#get data from the database
def get_data(data: dict):
    return collection.find_one(data)

