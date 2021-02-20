from bs4 import BeautifulSoup

with open("day11/index.html","r") as f:
    doc= f.read()
# Find
result= BeautifulSoup(doc,"html.parser")

print(result.find('div')) # first div
print(result.find_all('div')) # all divs in an array
print(result.find_all('div')[1]) # second div
print(result.find_all('div')[1].ul.find_all('li')) # all li inside of second div

for n in result.find_all('div'):
    print(n.h2) # all h2's inside divs

print(result.find_all('a'))
