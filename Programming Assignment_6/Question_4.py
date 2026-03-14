# 4. Write a Python Program to calculate the natural logarithm of any number?
import math

def log(num):
    return math.log(num)

def main():
    input_value=float(input("Enter a number : "))
    print(log(input_value))

if __name__=="__main__":
    main()