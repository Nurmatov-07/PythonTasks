
def input_number(var1): 
    try:
        if var1 < 0:
            raise ValueError ("Number is < 0: ")
        elif var1 % 2 == 0:
            raise TypeError ("Number is chetnoe")
        elif var1 > 10:
           raise IndexError ("Number is > 10")
    except ValueError :
        print("Number is < 0: ")
    except TypeError :
        print("Number is chetnoe")
    except IndexError :
        print("Number is > 10")

def main():
    a = float(input("Enter value: "))
    print(input_number(a))

main()