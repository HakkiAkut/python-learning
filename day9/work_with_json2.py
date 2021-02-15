data={
    1:{"id":1,
        "name": "hakki",
        "surname": "akut",
        "age": 22,
        "competencies": ["Python", "PHP", "Java"]
        }, 
    2:{"id":2,
        "name": "user1",
        "surname": "sur1",
        "age": 21,
        "competencies": ["Delphi", "C"]
        }
}

import json

with open("day9/user2.json","w") as file:
    json.dump(data,file,ensure_ascii=False)
with open("day9/user2.json","r") as file:
    data1=json.load(file)
print(data1)
print(data1["1"])
data1.update({"2": {"id": 2, "name": "user1", "surname": "sur1", "age": 21, "competencies": ["Delphi", "C","C++"]}})
# with data1.pop("2"), we can delete it also
with open("day9/user2.json","w") as file:
    json.dump(data1,file,ensure_ascii=False)