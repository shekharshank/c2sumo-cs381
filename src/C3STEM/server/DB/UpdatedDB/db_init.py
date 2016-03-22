import bcrypt
import sys
sys.path.insert(0, '/app/Middleware')

from problem_init import *
from DBUtil import *

db = DBUtil().getDatabase()
hashed_pass = bcrypt.hashpw("password".encode('utf-8'), bcrypt.gensalt())

###### FOR TESTING ONLY ######
db.problem_area.drop()
db.group.drop()
db.user.drop()
db.problem.drop()
###### END TEST ######

###### Problem Area ######
trafficArea = db.problem_area.insert_one({
    "_id": "Traffic",
    "problem_ids": [],
    "simulator": "SUMO"
}).inserted_id

###### Problems ######
initTrafficProblems(trafficArea)

###### Groups ######
groupList = []

# make 10 groups
for i in range (1, 11):
    num = str(i)
    groupID = db.group.insert_one({
        "name": "group" + num,
        "problem_area_id": trafficArea,
        "members": {},
        "collaboration_url": "http://google.com"
    }).inserted_id
    groupList.append(groupID)

###### Users ######
# make 30 users
for j in range (1, 31):
    num = str(j)
    groupNum = j % 10

    # make every 3rd user an admin
    userRole = "admin" if j % 3 == 0 else "user"

    user = db.user.insert_one({
        "_id": "user" + num,
        "first_name": "First" + num,
        "last_name": "Last" + num,
        "school_name": "School X",
        "school_id": "schoolx",
        "group_ids": [groupList[groupNum]],
        "password": hashed_pass,
        "change_password": True,
        "user_role": userRole
    }).inserted_id

    # add user to group, mapped to role
    db.group.update_one({"_id": groupList[groupNum]}, {"$set": {"members."+user: userRole}})
