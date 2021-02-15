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
data_list=[data,user1]
with open("day9/user1.json","r") as file:
    #json.dump(user1,file,ensure_ascii=False,indent=2)
    data2=json.load(file)
    data2.append(data)
    data2.append(user1)
    print(type(data2))
    print(data2)
with open("day9/user1.json","w") as file:
    json.dump(data2,file)