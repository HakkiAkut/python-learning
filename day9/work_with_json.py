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