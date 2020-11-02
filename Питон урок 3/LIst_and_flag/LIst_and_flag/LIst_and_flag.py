import random 

def register(list1, case = True):
    if(case):
        return list1.upper()
    else:
        return list1.lower()
    print(fun('My name is Salim', True))

def main():
    n = int(input("Enter size of list: "))
    arr = []
    i = 0
    for i in range(n):
        arr.append(random.randint(1, 50))
    print(register(arr, True))

main()