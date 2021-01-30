#generators doesn't hold place in memory, only creates current element and does the operation
def cube():
    for x in range(5):
        yield x**3  # yield makes generator
for i in cube():
    print(i)

generator=(i**3 for i in range(5)) # () using makes generator rather than using []
for i in generator:
    print(i)