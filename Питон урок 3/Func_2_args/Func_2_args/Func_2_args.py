
def new_func(var1, var2):
    if(var1 > 0 and var2 > 0):
        return var1 + var2
    elif(var1 < 0 and var2 < 0):
        return var1 - var2
    elif(var1 < 0 and var2 > 0 or var1 > 0 and var2 < 0):
        return 0

def main():
    res1 = int(input('Введите число 1: '))
    res2 = int(input('Введите число 2: '))
    print(new_func(res1, res2))

main()