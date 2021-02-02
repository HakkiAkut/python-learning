file=open("day7/file1.txt","w") # w means write
file.write("writed file\n")
file.write("writed file 2\n")
file.write("writed file 3\n")
print(file)
file.close()

with open("day7/file1.txt","a") as file: # a means append, appends string but doesn't clean file beforehand like write
    file.write("appended file\n")

with open("day7/file1.txt","r+") as file:# r+ means read and write same time. Cursor is important
    f=file.readlines()
    f.insert(3,"inserted 4th index\n")
    file.seek(0)
    file.writelines(f)