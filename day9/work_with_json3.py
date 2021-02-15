class User():
    def __init__(self,id,name,surname,competencies):
        self.id=id
        self.name=name
        self.surname=surname
        self.competencies=competencies

user= User(3,"user2","sur2",["Basic","Assembly"])
import json
print(user.__dict__)
users={
    user.id:user.__dict__
}
with open("day9/user3.json","w") as file:
    json.dump(users,file,ensure_ascii=False)
with open("day9/user2.json","r") as file:
    data=json.load(file)

for key,value in data.items():
    users.update({int(key):
        User(int(data[key]["id"]),data[key]["name"],data[key]["surname"],data[key]["competencies"]).__dict__})
with open("day9/user3.json","w") as file:
    json.dump(users,file,ensure_ascii=False)
print(users)