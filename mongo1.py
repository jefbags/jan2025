from pymongo import MongoClient

def connect_to_mongo(uri, db_name):
    client = MongoClient(uri)
    db = client[db_name]
    return db

# Example usage
if __name__ == "__main__":
    uri = "mongodb://localhost:27017/"
    db_name = "test"
    db = connect_to_mongo(uri, db_name)
    print(f"Connected to database: {db_name}")  

mycol = db["posts"]

# Find one document
x = mycol.find_one()
print(x)

# Find all documents
#for x in mycol.find():
#    print(x)

pydb = []
for x in mycol.find():
    pydb.append(x)

print(pydb)

print(pydb[1]['title'])

# This just updates the dictionary, not the database
pydb[1]['title'] = 'New Title'

# update function
#mycol.update_one({'_id': pydb[1]['_id']}, {"$set": {'title': 'New Title'}})