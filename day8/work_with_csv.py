import csv
# read as array
with open("day8/imdb_top_1000.csv", "r", encoding='UTF-8') as file:
    #print(file.read()) #read all
    csvfile=csv.reader(file)
    print("movies in 1994")
    with open("day8/movies.csv","w",encoding='UTF-8',newline='') as file: # w/o newline, blank lines appears
        csvfile1=csv.writer(file)
        csvfile1.writerow(["movie_name","movie_rating"])
        for p in csvfile:
            if p[2]=="1994":
                print(f"movie name:{p[1]}, movie rating:{p[6]}")
                csvfile1.writerow([p[1],p[6]])
    

# read as dictionary
with open("day8/imdb_top_1000.csv", "r", encoding='UTF-8') as file:
    csvfile2=csv.DictReader(file) #delimeter="|" parses with "|" rather than ","
    for p in csvfile2:
        if p['Released_Year']=="1994":
            print(p["Series_Title"])


