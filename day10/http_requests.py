import requests as req
import json

response=req.get("https://jsonplaceholder.typicode.com/todos")
print(response) # <Response [200]>
print(response.headers["Content-Type"]) # application/json; charset=utf-8
print(response.url) # https://jsonplaceholder.typicode.com/todos
print(response.encoding) # utf-8
print(type(response)) # <class 'requests.models.Response'>
print(type(response.text)) # <class 'str'>
print(type(json.loads(response.text))) # <class 'list'>
#print(response.text)

for i in json.loads(response.text):
    if(i["completed"]==True):
        print(i["title"])

# query strings

response= req.get("https://jsonplaceholder.typicode.com/todos",params={
    "completed":"true"
}) # only gets completed todos
for i in json.loads(response.text):
        print(i["title"])