from pymongo import MongoClient
from pymongo.server_api import ServerApi


def db_conn():
    client = MongoClient(
        "mongodb+srv://rodiongroshev:uK5UdDyi615a1jll@clusteredu.obrwfus.mongodb.net/?retryWrites=true&w=majority&appName"
        "=ClusterEdu",
        server_api=ServerApi('1')
    )
    db = client.book
    return db


def find_all():
    db = db_conn()
    res = db.hw.find({})
    for doc in res:
        print(doc)


def find_via_name(name):
    db = db_conn()
    match = db.hw.find_one({"name": name})
    return match


def update_age(name, new_age):
    db = db_conn()
    db.hw.update_one({"name": name}, {"$set": {"age": new_age}})


def update_features(name, new_feature):
    db = db_conn()
    db.hw.update_one({"name": name}, {"$push": {"features": new_feature}})


def delete_doc(name):
    db = db_conn()
    db.hw.delete_one({"name": name})


def delete_all():
    db = db_conn()
    db.hw.delete_many({})



if __name__ == '__main__':
    find_all()
    print(find_via_name("Tom"))
    # update_age("Tom", 5)
    # update_features("Sam", "bad boy")
    # delete_doc("Tom")
    # delete_all()
