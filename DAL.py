from db.mongoClient import client
from pymongo import UpdateOne
from Utility import brands
from tqdm import tqdm
db = client["bootcamp_team2"]  
collection = db["items"] 
class Record:
    def __init__(self,_id,created_at,massage_content,massage_type,**kwargs):
        self._id:str = _id
        self.created_at=created_at
        self.massage_content:str=massage_content
        self.massage_type:str=massage_type
        self.__dict__.update(kwargs)


def test(data:list[Record]):
    newdata = []
    data[0]["test"]=True
    newdata.append(data[0] )
    return data

def updateAll(updateFunction):
    # type: (callable[[list[Record]],list[Record]])->None
    """
    this function allow you to update rapidly the entier db 
    you have to pass a function that recive a list of records and return a list of updated records
    """
    print("fetching ...")
    data = collection.find()
    print("running update ...")
    modified_data= updateFunction(list(data))
    print("done!")
    print("building operation ...")
    
    
        
    bulk_operation=[
    UpdateOne({"_id":a["_id"]},{"$set":a},upsert=True) for a in modified_data
    ]
    print("done!")
    print("start pushing to DB ...")
    res =collection.bulk_write(bulk_operation)
    print("done!")
    


    




if __name__ == "__main__":
    updateAll(test)