import random

def two_lists(list1, flag):
    if(flag == True):
        for i in range(len(list1)):
            if(list1[i] % 2 != 0):
                return i;
    elif(flag == False):
        for j in range(len(list1)):
            if(list1[j] % 2 == 0):
                return j;

def main():
    n = int(input("Введите размер массива "))
    mas=[]
    for i in range(n):
        mas.append(random)
    flag = bool(input("Введите флаг "))
    print(two_lists(mas, flag))

main()
#    N = int(input("Введите размер массива "))
#    for res in range(N):
#        res = list(intput("Введите значение", res)
