from tinydb import TinyDB, Query

db = TinyDB('db.json')

def insert_data(data: dict):
    db.insert(data)

def get_data():
    return db.all()

def insert_file(file):
    db.insert(file)