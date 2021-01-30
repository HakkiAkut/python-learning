iterator=iter([1,2,3,4,5,6])
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

class Num():
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x=self.start
            self.start +=1
            return x
        else:
            raise StopIteration

lis2=Num(20,60)
num_iter=iter(lis2)
while True:
    try:
        print(next(num_iter))
    except StopIteration:
        break

def 

