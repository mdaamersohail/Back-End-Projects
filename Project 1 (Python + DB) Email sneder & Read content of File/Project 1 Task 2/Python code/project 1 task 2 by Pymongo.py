from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/', 27017)
print(client.list_database_names())

db = client['cars']

collection = db['ownbrands']

list1 =[{"name":"BMW","status":"confirmed"},{"name":"TESLA","status":"waiting for payment"},{"name":"FERRARI","status":"waiting for documentation"},{"name":"LAMBORGHINI","status":"confirmed"}]
res = collection.insert_many(list1)
print("car brands are added")
print(res.inserted_ids)

