from bs4 import BeautifulSoup

with open("day11/index.html","r") as f:
    doc= f.read()
# Attributes
result= BeautifulSoup(doc,"html.parser")

print(result.find(id="group3")) 
print(result.find(class_="group")) # first tag that has group class
print(result.find_all(class_="group")) # returns array
print(result.div.attrs["class"]) # return group

# css based
print(result.select('#header')) 
print(result.select('.group')) # returns array
print(result.select_one('.group')) # returns first

print(result.get_text(strip=True,separator=", ")) # returns all texts 
print(result.find('a').get('href')) # result.find('a')['href'] works too