import pymongo
from bson import ObjectId


def insert_data(data):
    """
    Insert new data or document in collection
    :param data:
    :return:
    """
    document = collection.insert_one(data)
    return document.inserted_id
def update_or_create(document_id, data):
    """
    This will create new document in collection
    IF same document ID exist then update the data
    :param document_id:
    :param data:
    :return:
    """
    # TO AVOID DUPLICATES - THIS WILL CREATE NEW DOCUMENT IF SAME ID NOT EXIST
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data}, upsert=True)
    return document.acknowledged
def get_single_data(document_id):
    """
    get document data by document ID
    :param document_id:
    :return:
    """
    data = collection.find_one({'_id': ObjectId(document_id)})
    return data
def get_multiple_data(collection):
    """
    get document data by document ID
    :return:
    """
    data = collection.find()
    return list(data)
def print_all(collection):
    print("\n")
    for x in collection.find():
        print(x)
    print("\n")
def update_existing(document_id, data):
    """
    Update existing document data by document ID
    :param document_id:
    :param data:
    :return:
    """
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data})
    return document.acknowledged
def remove_data(document_id):
    document = collection.delete_one({'_id': ObjectId(document_id)})
    return document.acknowledged




#def insert_document(collection, data):
#    """ Function to insert a document into a collection and
#    return the document's id.
#    """
#    return collection.insert_one(data).inserted_id


#def insert_document(collection, data):
#    """ Function to insert a document into a collection and
#    return the document's id.
#    """
#    return collection.insert_one(data).inserted_id


#def find_document(collection, elements, multiple=False):
#    """ Function to retrieve single or multiple documents from a provided
#    Collection using a dictionary containing a document's elements.
#    """
#    if multiple:
#        results = collection.find(elements)
#        return [r for r in results]
#    else:
#        return collection.find_one(elements)

#def print_all(collection):
#    for x in collection.find():
#        print(x)


#def uodate_info(collection,_id):
#    for i in collection:
#        if _id == colletcion._id:
#            pass

#def find_by_login(users_collection,login):
#    query = {"login":login}
#    doc = users_collection.find(query)
#    for x in doc:
#        print(x)

#def sort_by(collection,parameter):
#    doc = collection.find().sort(parameter)
#    for x in doc:
#        print(x)
    


#def insert_document(collection, data):
#    """ Function to insert a document into a collection and
#    return the document's id.
#    """
#    return collection.insert_one(data).inserted_id


#def insert_document(collection, data):
#    """ Function to insert a document into a collection and
#    return the document's id.
#    """
#    return collection.insert_one(data).inserted_id


#def find_document(collection, elements, multiple=False):
#    """ Function to retrieve single or multiple documents from a provided
#    Collection using a dictionary containing a document's elements.
#    """
#    if multiple:
#        results = collection.find(elements)
#        return [r for r in results]
#    else:
#        return collection.find_one(elements)

#def print_all(collection):
#    for x in collection.find():
#        print(x)


#def uodate_info(collection,_id):
#    for i in collection:
#        if _id == colletcion._id:
#            pass

#def find_by_login(users_collection,login):
#    query = {"login":login}
#    doc = users_collection.find(query)
#    for x in doc:
#        print(x)

#def sort_by(collection,parameter):
#    doc = collection.find().sort(parameter)
#    for x in doc:
#        print(x)
    


