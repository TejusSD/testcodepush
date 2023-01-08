#hitting another ineuron mongodb dabase
import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.glvnm2e.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)
