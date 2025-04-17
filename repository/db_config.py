from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = 'mongodb://localhost:27017/'
server_api = ServerApi('1')

client = MongoClient(uri,server_api=server_api)

try:
    client.admin.command('Ping')
    
    print(f"Pinged your deployment. You successfully connected to MongoDB!")
    
except Exception as e:
    print(e)

db = client.auto_submit
collection = db["auto_submit_data"]