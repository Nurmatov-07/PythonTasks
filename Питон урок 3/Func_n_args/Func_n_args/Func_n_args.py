import random

def adder(nums):
    max = nums[0]
    for k in range(1, len(nums)):
        if nums[k] > max:
            max = nums[k]
    return max

def main():
    #n = int(input("Введите размер массива: " ))
    #for res in range(n):
    #    res = split(input("Введите список чисел: "))
    #print(adder(res))
    items = [random.randint(0, 50) for i in range(50)]
    print(items)
    print("Максимальное число {}".format(adder(items)))

main()