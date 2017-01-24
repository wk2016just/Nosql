from pymongo import MongoClient

mc = MongoClient("localhost",27017)

db = mc.users

db.users.save({"name":"python","age":10})

c = db.users.find()

for o in c:
    print(o)

mc.close()