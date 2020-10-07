def dif():
    arr1 = []
    arr2 = []
    for i in range(1, 100):
        if i % 7 == 0:
            arr1.append(i)
        else:
            arr2.append(i)
    print("Числа которые делятся на 7: {0} \n Числа которые не делятся на 7 {1}".format(arr1, arr2))

dif()