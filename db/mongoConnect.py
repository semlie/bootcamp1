import pymongo
from bson import ObjectId
import os 

from dotenv import load_dotenv

load_dotenv()


CONNECTION_STRING =os.getenv('CONNECTION_STRING')



client = pymongo.MongoClient(CONNECTION_STRING)
db = client["bootcamp_team2"]  
collection = db["users"]  

def create_document(data):
    result = collection.insert_one(data)
    return result.inserted_id

def read_documents(filter=None, projection=None):
    cursor = collection.find(filter=filter, projection=projection)
    return list(cursor)

def update_document(document_id, update_data):
    result = collection.update_one({"_id": ObjectId(document_id)},
                                   
                                    {"$set": update_data},upsert=True
                                    )
    return result.modified_count

def delete_document(document_id):
    result = collection.delete_one({"_id": ObjectId(document_id)})
    return result.deleted_count

# Example usage
# new_document_id = create_document({"name": "nadavv", "age": 151})
# print("Created document with ID:", new_document_id)

# documents = read_documents(filter={"age": {"$gt": 25}}, projection={"name": 1, "_id": 0})
# print("Documents with age over 25 (names only):", documents)

# update_document("65d246fe3d0f4ea8ab019a55", {"age": 745})
# print("Updated document age to")

# deleted_count = delete_document("65d246fe3d0f4ea8ab019a55")
# print("Deleted document:", deleted_count)

client.close()
