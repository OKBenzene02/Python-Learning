import requests

BASE = "http://127.0.0.1:5000/"

headers = {"Content-Type": "application/json"}

sample_data = [
    {"likes": 12300, "name": "lilly", "views": 10324},
    {"likes": 123223, "name": "diff", "views": 100},
    {"likes": 122233, "name": "fc5", "views": 1223300},
    {"likes": 1231313, "name": "dying light", "views": 10230},
    {"likes": 123413434, "name": "fh5", "views": 10454200}
]

for i, data in enumerate(sample_data):
    response = requests.put(BASE + "video/" + str(i), json=data, headers=headers)
    print(response.json())

input()
response = requests.get(BASE + "video/3", headers=headers)
print(response.json())
input()

response = requests.delete(BASE + "video/2", headers=headers)
print(response)
