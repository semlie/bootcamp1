from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

client = MongoClient(getenv('CONNECTION_STRING'))
 
