from db import mongoConnect
import os
from flask import Flask, jsonify, request
app = Flask(__name__)
from dotenv import load_dotenv
import json

load_dotenv()
print(os.getenv('CONNECTION_STRING'))

@app.route("/items", methods=["GET"])
def get_data():
    page = int(request.args.get("page",0))
    per_page = 100
    if not page:per_page = page = 0
    data = list(mongoConnect.collection.find().skip((page - 1) * per_page).limit(per_page))
    print(page)
    return jsonify(json.loads( json.dumps(data,default=str)))





@app.route("/updateItems",methods=["PUT"])
def update_items():
    filter = {}
    update = {}
    resp = mongoConnect.collection.update_many(filter,update)
    brands = ["samsung", "apple"]

    # Update documents where text contains any of the brands
    mongoConnect.collection.update_many({"text": {"$in": brands}}, {"$set": {"entity.brand": {"$in": brands}}})





# @app.route("/phone",methods=["GET"])
# def get_specific_phone():


# filter = {
#     "$and": [
#         {"massage_content": {"$regex": "iphone", "$options": "i"}},
#         {"category": {"$in": ["buy", "sale"]}}
#     ]
# }

# # Perform the query
# results = mongoConnect.collection.find(filter)

# # Iterate over the results and process them as needed
# for document in results:
#     print(document)
    






# @app.route("/data", methods=["POST"])
# def post_data():
#     new_data = request.json
#     mongoConnect.collection.insert_one(new_data)
#     return "Data added successfully", 201


@app.route('/')
def index():
    '''
    Index page
    '''
    return jsonify(dict(name='John', age=25, city='New York'))


if __name__ == '__main__':
    app.run('127.0.0.1', port=8000,   )


