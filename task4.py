"""
JSON handling
requests, simplejson module (json)

"""

import requests as req
import simplejson as json

#getting data
res = req.get("http://jsonplaceholder.typicode.com/todos")
data = json.loads(res.text)

#writing to file
with open("some.json", "w") as f:
    f.write(res.text)

#processing
users = dict()

for i in data:
    if users.get(i["userId"]) == None:
        users[i["userId"]] = {"tasks":0, "completed":0}

print("total users: {}".format(len(users.keys())))

for i in data:
    id = i["userId"]
    users[id]["tasks"] += 1
    if i["completed"] == True:
        users[id]["completed"] += 1

for i in users.keys():
    print("user №{} -> tasks:{} , completed:{}".\
          format(i, users[i]["tasks"],users[i]["completed"]))