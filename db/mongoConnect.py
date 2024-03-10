import os 
import pickle
import pymongo
from bson import ObjectId
from bson import Binary


from dotenv import load_dotenv

load_dotenv()


CONNECTION_STRING =os.getenv('CONNECTION_STRING')



client = pymongo.MongoClient(CONNECTION_STRING)
db = client["bootcamp_team2"]  
collection = db["items"]  

def create_document(data):
    """craeting new data"""
    result = collection.insert_one(data)
    return result.inserted_id

def read_documents(filter=None, projection=None):
    """reading data"""
    cursor = collection.find(filter=filter, projection=projection)
    return list(cursor)

def update_document(document_id, update_data):
    """updating data"""
    result = collection.update_one({"_id": ObjectId(document_id)},
                                   
                                    {"$set": update_data},upsert=True
                                    )
    return result.modified_count

def delete_document(document_id):
    """deleting data"""
    result = collection.delete_one({"_id": ObjectId(document_id)})
    return result.deleted_count

# Example usage
# new_document_id = create_document({"name": "nadavv", "age": 151})
# print("Created document with ID:", new_document_id)

# documents = read_documents(filter={"age": {"$gt": 25}}, projection={"name": 1, "_id": 0})
# print("Documents with age over 25 (names only):", documents)

# update_document("65d246fe3d0f4ea8ab019a55", {"age": 745})
# print("Updated document age to")


def display_dictionaries(data):
    values = [value    for key, value in data.items()]
    try:
        collection.insert_many(values)
    except Exception as e:
        print(e)

# deleted_count = delete_document("65d246fe3d0f4ea8ab019a55")
# print("Deleted document:", deleted_count)


with open('data/filterd.pkl', 'rb') as f:
    data = pickle.load(f)
    display_dictionaries(data)





# client.close()

