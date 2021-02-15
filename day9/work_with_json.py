import json
with open("day9/user.json","r") as file:
    data=json.load(file)
print(data,type(data))
print(data["competencies"][0])

str1="""
{
    "name":"hakki",
    "surname":"akut",
    "age":22,
    "competencies":[
        "Python","PHP","Java"
    ]
    
}
"""
data1=json.loads(str1) # used loads bcs its string not json file
print(data["competencies"][0])

# json serializing

user1= {
    "name":"user1",
    "surname":"sur1",
    "age":21,
    "competencies":["Delphi","C"]
}
print(user1,type(user1))
serial=json.dumps(user1,ensure_ascii=False,indent=2)# turned to string
print(type(serial))
print(serial)
with open("day9/user.json","r+") as file:
    json.dump(user1,file,ensure_ascii=False,indent=2)