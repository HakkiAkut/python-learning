def decoretor(func):
    def wrapper(param):
        print("premise operations")
        func(param)
        print("rear operations")
    return wrapper

@decoretor
def main_func(param):
    print(f"Main operation {param}")

main_func(1)