# 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
def binary(value):
    return bin(value)[2:]

def octal(value):
    return oct(value)

def hexa(value):
    return hex(value)

def main():
    print("1. Binary\n2. Octal\n3. Hexadecimal\nEnter you choice of number")
    input_value=int(input())
    input_num=int(input("Enter number to convert : "))
    if input_value==1:
        print(binary(input_num))
    elif input_value==2:
        print(octal(input_num))
    elif input_value==3:
        print(hexa(input_num))
    else:
        print("Please check again")

if __name__=="__main__":
    main()