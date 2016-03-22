import csv
from datetime import datetime
import sys
import bcrypt
sys.path.insert(0, '/app/Middleware')

from DBUtil import *

db = DBUtil().getDatabase()

with open('users.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
    	hashed_pass = bcrypt.hashpw(row[1].encode('utf-8'), bcrypt.gensalt())
    	db.user.save({'_id' : row[0], 'password' : hashed_pass})
