from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
from pprint import pprint
uri = "mongodb+srv://keerthi2556:Reddy2002@cluster0.eaiaoy5.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

   
    db = client.Monthly_Expense

    # Get reference to 'accounts' collection
    accounts_collection = db.Transactions

    # inserting one account
    documents_to_find = {"Type":"Cash"}

    # Write an expression that selects the documents matching the query constraint in the 'accounts' collection.
    cursor = accounts_collection.find(documents_to_find)

    num_docs = 0
    for document in cursor:
        num_docs += 1
        pprint.pprint(document)
        print()
    print("# of documents found: " + str(num_docs))


except Exception as e:
    print(e)
finally:
    client.close()
