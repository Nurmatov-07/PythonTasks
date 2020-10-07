    
def max_min():
    new_tuple = (23.4, 54.123, -5.4344, -99.1, 4.1, 0.999, 78.78, 98.123, 12.21, 1.11)
    i = 0
    max = 0
    min = 0
    for j in range(0, len(new_tuple)):
        for i in range(0, len(new_tuple)):
            if new_tuple[i] > max:
                max = new_tuple[i]
            if new_tuple[i] < min:
                min = new_tuple[i]
    print(new_tuple)
    print('Maximum value: {0}, \n Minimum value: {1}'.format(max, min))
        
max_min()