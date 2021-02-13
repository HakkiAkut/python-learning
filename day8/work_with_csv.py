import csv
# read as array
with open("day8/imdb_top_1000.csv", "r", encoding='UTF-8') as file:
    #print(file.read()) #read all
    csvfile=csv.reader(file)
    print("movies in 1994")
    for p in csvfile:
        if p[2]=="1994":
            print(f"movie name:{p[1]}, movie rating:{p[6]}")

# read as dictionary
with open("day8/imdb_top_1000.csv", "r", encoding='UTF-8') as file:
    csvfile1=csv.DictReader(file)
    for p in csvfile1:
        if p['Released_Year']=="1994":
            print(p["Series_Title"])

