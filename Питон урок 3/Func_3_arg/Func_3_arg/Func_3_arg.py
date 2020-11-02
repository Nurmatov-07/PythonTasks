
def new_func(var1, var2, var3):
    arr = [var1, var2]
    node1 = max(arr)
    arr1 = [var2, var3]
    node2 = max(arr1)
    return max(node1, node2)

def main():
    res1 = int(input("Ведите число: "))
    res2 = int(input("Ведите число: "))
    res3 = int(input("Ведите число: "))
    print(new_func(res1, res2, res3))

main()