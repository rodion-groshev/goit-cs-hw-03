from pymongo import MongoClient
from pymongo.server_api import ServerApi


def create_one(document: dict):
    client = MongoClient(
        "mongodb+srv://rodiongroshev:uK5UdDyi615a1jll@clusteredu.obrwfus.mongodb.net/?retryWrites=true&w=majority&appName"
        "=ClusterEdu",
        server_api=ServerApi('1')
    )
    db = client.book
    return db.hw.insert_one(document).inserted_id


def create_many(document: list):
    client = MongoClient(
        "mongodb+srv://rodiongroshev:uK5UdDyi615a1jll@clusteredu.obrwfus.mongodb.net/?retryWrites=true&w=majority&appName"
        "=ClusterEdu",
        server_api=ServerApi('1')
    )
    db = client.book
    return db.hw.insert_many(document).inserted_ids


if __name__ == '__main__':
    print(create_one({
        "name": "Tom",
        "age": 4,
        "features": ["white", "annoying", "angry"]
    }))
    print(create_many([
        {
            "name": "Kyle",
            "age": 2,
            "features": ["black", "good boy"]
        },
        {
            "name": "Sam",
            "age": 4,
            "features": ["Grey", "annoying"]
        }
    ]))
