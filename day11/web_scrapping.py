from bs4 import BeautifulSoup

with open("day11/index.html","r") as f:
    doc= f.read()

result= BeautifulSoup(doc,"html.parser")

print(result.prettify())
print(type(result))
print(result.title.string)
print(result.body.h1.string)
print(result.body.div.h2.string)