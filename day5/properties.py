class Product:
    def __init__(self,name,price):
        self.name = name
        if price >=0:
            self._price = price
        else:
            raise ValueError("price can't be negative")
    
    def __str__(self):
        return f"{self.name} {self._price}"
    def __repr__(self):
        return f"{self.name} {self._price}"
    def __len__(self):
        return len(self.name)
    def __del__(self):
        print("object is deleted")
    #returns price(getter)
    @property
    def price(self):
        return self._price
    #sets price(setter)
    @price.setter
    def price(self,value):
        if value >=0:
            self._price = value
        else:
            raise ValueError("price can't be negative")

class NewDict(dict):
    def __repr__(self):
        print("repr method message")
        return super().__repr__()
    def __missing__(self,key):
        print("there is no such item")

n1 = NewDict({"a":"A"})
print(n1)
print(n1["b"])