import pymongo
client = pymongo.MongoClient("mongodb+srv://tejus:tejus123@cluster0.glvnm2e.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)


d={
    "name":"tejus",
    "email":"tejas.sd5@gmail.com",
    "surname":"sd"
}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d )