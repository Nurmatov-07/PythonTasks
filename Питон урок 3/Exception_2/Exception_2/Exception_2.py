import random

def list_exception(var1, idx1):
    try:
        for i in range(len(var1)):
            if idx1 != var1[i]:
                raise IndexError('Index out of range!')
            else:
                continue
    except IndexError:
        print("Incorrect index, try again \n")
    except ValueError:
        print("Invalid value!: ")

def main():
    arr = []
    N = int(input("Enter the size of list: "))
    for i in range(N):
        arr.append(random.randint(0, 50))
    idx = int(input("Enter the index: "))
    print(list_exception(arr, idx))

main()