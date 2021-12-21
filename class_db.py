import pymongo
# import mysql.connector

from datetime import datetime


class class_db:
    myclient = None
    DB_NAME = "Proxy_Pool"
    DB_COLLECTION_ACTIVE = "working"
    DB_COLLECTION_NON_ACTIVE = "expired"
    DB_SORT_ASC = 1
    DB_SORT_DESC = -1

    Proxy_Schema = {
        "_id": "",
        "ip": "",
        "port": "",
        "proxy": "",
        "status": "working",
        "response_time": 0
    }

    def parse_Schema(self, ip, proxy, responsetime, working=True):
        Schema = self.Proxy_Schema
        Schema["_id"] = str(ip).replace(".", "").replace(":", "")
        Schema["ip"] = str(ip).split(":")[0]
        Schema["port"] = str(ip).split(":")[1]
        Schema["proxy"] = proxy
        Schema["response_time"] = responsetime
        if working:
            Schema["status"] = "working"
        else:
            Schema["status"] = "expired"

        return Schema

    def __del__(self):
        self.myclient.close()

    def __init__(self):
        # self.myclient = pymongo.MongoClient("mongodb://admin:Zero0One10@64.225.84.136:27017/")
        # self.myclient = pymongo.MongoClient(
        #     'mongodb+srv://jay:iW03MQDf5GzAwNPj@cluster0.cv7n8.mongodb.net/test?authSource=admin&replicaSet=atlas-58cywz-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
        # self.myclient = pymongo.MongoClient('mongodb://admin:OmegaKnee@34.93.192.68:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false')
        self.myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017')
        self.mydb = self.myclient[self.DB_NAME]

    def add_working_ip(self, ip, proxy1, res_time):
        try:
            self.db_insert_single(self.DB_COLLECTION_ACTIVE, self.parse_Schema(ip, proxy1, res_time))
        except pymongo.errors.DuplicateKeyError:
            print("duplicate")

    def db_insert_single(self, collection, data):
        mycol = self.mydb[collection]
        mycol.insert_one(data)

        # print(self.mydb[collection])

    def db_insert_many(self, collection, data):
        mycol = self.mydb[f"{collection}"]
        mycol.insert_many(data)

    def db_select(self, collection, query="{}", limit=0, sort=""):
        mycol = self.mydb[collection]

        if limit:
            if sort:
                return list(mycol.find().limit(limit).sort(sort["name"], sort["order"]))
            return list(mycol.find().limit(limit))

        if sort:
            return list(mycol.find().sort(sort["name"], sort["order"]))

        return list(mycol.find())

    def db_delete_one(self, collection, query):
        mycol = self.mydb[f"{collection}"]
        # myquery = {"address": "Mountain 21"}
        mycol.delete_one(query)

    def db_update_one(self, collection, query, newdata):
        mycol = self.mydb[f"{collection}"]
        # myquery = {"address": "Valley 345"}
        newvalues = {"$set": newdata}
        mycol.update_one(query, newvalues)
