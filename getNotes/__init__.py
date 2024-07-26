import azure.functions as func
import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
        try:
            url = os.environ["MyDbConnection"]
            client = pymongo.MongoClient(url)
            database = client['newdblabserverless']
            collection = database['notes']

            result = collection.find({})
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except ConnectionError as e:
            return func.HttpResponse("Database connection error.", status_code=500)
