# lists
int_list= [1,2,4,5]
obj_list = [1,"str",True,1.2]
print("{} {}".format(int_list,obj_list))
print(f"{int_list} {obj_list}")
print(len(obj_list+int_list))
lists_list=[int_list,obj_list]
print(lists_list[0][1])
print("str" in obj_list) # checks is there a "str" in obj_list
print(obj_list[-1]) # returns last
print(int_list[:3]) # first 3
print(int_list[-3:]) # last 3
print(int_list[::2]) # every 2 element
print(int_list[::-1]) # reverse 

# list methods
print(min(int_list))
print(max(int_list))
int_list.append(9)
int_list.insert(3, 24)
print(int_list)
print(int_list.pop())
int_list.sort()
int_list.reverse()
print(int_list)
print(int_list.index(4))
print(int_list.count(2))
int_list.clear()
print(int_list)

# tuple 
tuple1=(1,3)
# similar to lists, just can't change elements like tuple[0]=5

#dictionary
dic = {4:"four", 14:"fourteen",2:"two"}
print(dic[14])
dic[21]="twenty-one"
print(dic[21])

user ={
    1: {
        "id":1,
        "name": "one",
        "pwd":1,
    },
    2: {
        "id":2,
        "name": "two",
        "pwd":2,
    }
}
print(user[1]["name"])

# dictionary methods
user.update({
    3:{
        "id":3,
        "name": "3",
        "pwd":3,
    }
})
for item in user:
    print(user[item])

for item in user.keys():
    print(item)
user.popitem()

for x,y in user.items():
    print(x,y)
del user # deletes object(dictionary for this case)

# sets - no duplicate, not indexable 
a = set([1,2,3,4,1,2])
for item in a:
    print(item)