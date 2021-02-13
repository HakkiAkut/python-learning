import csv
# read as array
with open("day8/imdb_top_1000.csv", "r", encoding='UTF-8') as file:
    #print(file.read()) #read all
    csvfile=csv.reader(file)
    print("movies in 1994")
    # csv writing
    with open("day8/movies1994.csv","w",encoding='UTF-8',newline='') as file: # w/o newline, blank lines appears
        csvfile1=csv.writer(file)
        csvfile1.writerow(["released_year","movie_name","movie_rating"])
        for p in csvfile:
            if p[2]=="1994":
                print(f"movie name:{p[1]}, movie rating:{p[6]}")
                csvfile1.writerow([p[2],p[1],p[6]])
    

# read as dictionary
with open("day8/imdb_top_1000.csv", "r", encoding='UTF-8') as file:
    csvfile2=csv.DictReader(file) #delimeter="|" parses with "|" rather than ","
    # csv dict writer
    with open("day8/movies1995-6.csv","w",encoding='UTF-8',newline='') as file:
        csvfile3=csv.DictWriter(file,["Released_Year","Series_Title","IMDB_Rating"])
        csvfile3.writeheader()
        for p in csvfile2:
            if p['Released_Year']=="1995":
                print(p["Series_Title"])
                csvfile3.writerow({"Released_Year":p['Released_Year'],
                "Series_Title":p["Series_Title"],
                "IMDB_Rating":p["IMDB_Rating"]})
with open("day8/imdb_top_1000.csv", "r", encoding='UTF-8') as file:
    csvfile2=csv.DictReader(file) 
    # if we already add header then open as append rather than write
    with open("day8/movies1995-6.csv","a",encoding='UTF-8',newline='') as file:
        csvfile4=csv.DictWriter(file,["Released_Year","Series_Title","IMDB_Rating"])
        for p in csvfile2:
            if p['Released_Year']=="1996":
                print(p["Series_Title"])
                csvfile4.writerow({"Released_Year":p['Released_Year'],
                "Series_Title":p["Series_Title"],
                "IMDB_Rating":p["IMDB_Rating"]})

