from db.mongoClient import client
from Utility import brands
from tqdm import tqdm
db = client["bootcamp_team2"]  
collection = db["items"] 

def UpdateALLBrands():  
    # Start a session
    with client.start_session() as session:
    # Start a transaction
         with session.start_transaction():
             data = collection.find({})
             for  record  in tqdm( data) :
                 
                 message = record.get("massage_content","").lower()
                 for brand in brands:
                    if brand.lower() in message:
                        collection.update_one({"_id": record["_id"]}, {"$addToSet": {"brands": brand}},upsert=True)
             session.commit_transaction()

if __name__ == "__main__":
    UpdateALLBrands()