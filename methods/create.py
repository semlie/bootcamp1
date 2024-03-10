# import pymongo


# from monngoConnect import users

# def create_document(document):
#     try:
#         result = users.insert_one(document)
#         print("Document created:", result.inserted_id)
#     except pymongo.errors.OperationFailure as e:
#         print("Creation failed:", e)

# # Example usage:
# new_document = {"name": "Charlie", "age": 25, "city": "Paris"}
# create_document(new_document)