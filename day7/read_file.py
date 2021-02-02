f=open("day7/file.txt","r") # r means read
print(f)
print(f.read())
print(f.seek(0)) #changes location of cursor, after read() method, it will return string start to end,
# and cursor will be at the end. After adding something and try to read() again it will continue from where cursor is.
# not start point
f1=f.readlines()
for x in f1:
    print(x)
f.close()

with open("day7/file.txt","r") as file: # it will close automatically
    print(file.read(5))
    print(file.tell())
    print(file.read())
try:
    print(file.tell())
except ValueError:
    print("file is closed!")
