from bson.json_util import dumps

class ServiceModel():

    def __init__(self, collection):
        self.collection = collection

    def query_service(self, query):
        records_fetched = self.collection.find(query)
        if self.collection.count_documents(query) > 0:
            return dumps(records_fetched)
        else:
            return []

