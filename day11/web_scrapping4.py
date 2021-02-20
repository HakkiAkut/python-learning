from bs4 import BeautifulSoup

with open("day11/index.html","r") as f:
    doc= f.read()
# Navigating
result= BeautifulSoup(doc,"html.parser")

print(result.head) # html head tag
print(result.body.div.contents) # first div's contents(array)
print(result.body.div.contents[1])
print(result.body.div.contents[3].contents)

for c in result.body.div.children: 
    if c !="\n":
        print(c)
for c in result.body.div.descendants: 
    if c !="\n":
        print(c)

print(result.body.div.next_sibling.next_sibling)
print(result.find(id="third").previous_sibling.previous_sibling)
print(result.find(id="third").find_previous_sibling('li'))
print(result.find(id="third").parent)
print(result.find(id="third").find_parent('div'))