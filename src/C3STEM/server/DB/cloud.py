from bson.objectid import ObjectId
from DBUtil import *

db = DBUtil().getDatabase()

ip = "X.X.X.X"
db.virtualmachine.insert({
    "_id": ip,
    "flavor": "m1.medium",
    "private_IP": 'X.X.X.X',
    "public_IP": ip,
    "key_name": "c3stem_keypair",
    "type": "TRANSIENT",
    "status": "AVAIL",
    "user": "ALL",
    "mode": "GROUP"
});

ip = "X.X.X.X"
db.virtualmachine.insert({
    "_id": ip,
    "flavor": "m1.medium",
    "private_IP": 'X.X.X.X',
    "public_IP": ip,
    "key_name": "c3stem_keypair",
    "type": "TRANSIENT",
    "status": "AVAIL",
    "user": "ALL",
    "mode": "GROUP"
});
