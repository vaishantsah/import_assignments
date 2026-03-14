# 2. Write a Python Program to Find Factorial of Number Using Recursion?
def fact(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    else:
        return num * fact(num-1)
    
def main():
    input_value=int(input("Enter a number : "))
    result=(fact(input_value))
    print(result)

if __name__=="__main__":
    main()