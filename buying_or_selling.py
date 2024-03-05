from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

mongo_connection = os.environ.get("MONGO_DB")
client = MongoClient(mongo_connection)
db = client.get_database()

result_mongo = []
result_local = []

def get_data_from_mongodb():
    collection = db["items"]  
    data = collection.find()
    calculate_of_data(data)


def calculate_of_data(data):
    global result_local
    result_local = []
    count_selling = 0
    count_buying = 0
    count_both = 0
    count_other = 0
    for document in data:
        content = document["massage_content"]
        intent = check_intent(content)
        if(intent=="selling"):
            count_selling+=1
            result_local.append('sale')
        elif(intent=="buying"):
            count_buying+=1
            result_local.append('buy')
        elif(intent=="both buying and selling"):
            count_both+=1
            result_local.append('both')
        else:
            count_other+1
            result_local.append('other')
    print_of_count_data(count_selling,count_buying,count_both,count_other)


def print_of_count_data(count_selling,count_buying,count_both,count_other):
    print("selling_me:",count_selling)
    print("buying_me:",count_buying)
    print("both buying and selling:",count_both)
    print("other:",count_other)
    print("--------------")


def check_intent(text):
    intent_to_sell_words = [
        "Wts", "For sale", "Selling", "Offer", "Sell", "Available",
        "Clearing out", "Disposing of", "Offloading", "Auctioning",
        "Liquidating", "Putting up for sale", "Unloading", "Offering up", "Letting go",
        "Shipment"
    ]
    intent_to_buy_words = [
        "Wtb", "Looking for", "Seeking", "Buying", "Wanting", "Purchasing",
        "In search of", "Interested in", "Acquiring", "Needing", "Hunting for",
        "Requesting", "Shopping for", "Hoping to buy", "Wanting to acquire","buy",
        "Looking to buy","purchase"
    ]
    both_intent_words = [
        "Trading", "Bartering", "Exchange", "Swap", "Trade-in", "Deal",
        "Negotiating", "Transaction", "Dealings", "Business", "Commerce",
        "Market", "Exchange", "Offer", "Bid","For sale or buying","Selling or buying"
    ]

    intent_to_sell = any(word.lower() in text.lower() for word in intent_to_sell_words)
    intent_to_buy = any(word.lower() in text.lower() for word in intent_to_buy_words)
    both_intent = any(word.lower() in text.lower() for word in both_intent_words)

    if both_intent:
        return 'both buying and selling'
    elif intent_to_sell:
        return 'selling'
    elif intent_to_buy:
        return 'buying'
    else:
        return 'none of them!'


def check_matching_errors(data):
    error_count = 0
    for item in data:
        content = item["massage_content"]
        category = item["category"]
        inferred_intent = check_intent(content)
        if (category == "sale" and inferred_intent != "selling") or (category == "buy" and inferred_intent != "buying") or (category == "both" and inferred_intent != "both buying and selling"):
            error_count += 1
    return error_count


def count_buy_and_sale(data):
    global result_mongo
    result_mongo = []
    count_sale = 0
    count_buy = 0

    for item in data:
        categoty = item["category"]
        if(categoty=="sale"):
            count_sale+=1
            result_mongo.append('sale')
        elif(categoty=="buy"):
            count_buy+=1
            result_mongo.append('buy')
        else:
            result_mongo.append('other')
    print("sale_mongo:",count_sale)
    print("buy_mongo:",count_buy)

# Fetch data from MongoDB and apply checks
get_data_from_mongodb()

# Calculate matching errors
error_count = check_matching_errors(db["items"].find())
total_items = db["items"].count_documents({})
print("Total items:", total_items)
print("Matching errors:", error_count)
print("Percentage of matching errors: {:.2f}%".format((error_count / total_items) * 100))
count_buy_and_sale(db["items"].find())

print("result_local:",len(result_local))
print("result_mongo:",len(result_mongo))

