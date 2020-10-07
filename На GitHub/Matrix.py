
def matx():
    count = 0
    my_array = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12]]
    for i in range(len(my_array)):
        print(my_array[i])
        count += 1
    new_arr = 0
    for i in range(len(my_array[0])):
        new_arr = my_array[0]
        new_arr += (my_array[i + 1])
    print(new_arr)
    n = 0
    for j in range(3):
        for k in range(n, len(new_arr), 3):
            print(new_arr[k])
        n += 1
matx()