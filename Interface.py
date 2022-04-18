import requests
import json

url = "http://127.0.0.1:8888/api/login"
data = json.dumps({"name": '周baby', "password": '123'})
headers = {"Content-Type": "application/json"}
print(data)
res = requests.post(url=url, data=data, headers=headers)

print(res.json())

