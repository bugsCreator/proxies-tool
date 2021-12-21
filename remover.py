from class_db import class_db
from class_main import class_main
import pymongo
from time import sleep

db = class_db()
main = class_main()

sort = {}
sort["name"] = "response_time"
sort["order"] = db.DB_SORT_ASC
while True:
    proxies = db.db_select(db.DB_COLLECTION_ACTIVE)
    for proxy in proxies:
        res = main.proxies_checker(proxy["proxy"])
        _id = proxy["_id"]
        ip = f"{proxy['ip']}:{proxy['port']}"
        if res:
            # working
            db.db_update_one(db.DB_COLLECTION_ACTIVE, {"_id": _id}, proxy)
            print("working", ip)
        else:
            # expired

            proxii = proxy["proxy"]
            try:
                db.db_insert_single(db.DB_COLLECTION_NON_ACTIVE, db.parse_Schema(ip, proxii, None, working=False))
            except pymongo.errors.DuplicateKeyError:
                pass
            db.db_delete_one(db.DB_COLLECTION_ACTIVE, {"_id": _id})
            print("not working", ip)

    print('\n---------------------DONE-------------------\n')
    sleep(60 * 15)
