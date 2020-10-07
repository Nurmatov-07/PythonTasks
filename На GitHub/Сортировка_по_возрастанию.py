
def sort():
    i = 0
    first_list = [22, 98, -1, 0, 56, -99]
    length = len(first_list)
    for j in range(0, length - 1):
        for i in range(0, length - j - 1):
            if first_list[i] > first_list[i + 1]:
                c = first_list[i]
                first_list[i] = first_list[i + 1]
                first_list[i + 1] = c
                i += 1
    print(first_list)

sort()