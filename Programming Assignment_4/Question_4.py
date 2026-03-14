# 4. Write a Python Program to Check Armstrong Number?
def check_armstrong(num:str):
    length=len(num) #used as a power multiplier
    result=0 # Initialize the comparing variable
    for i in range(0,length):
        result+=int(num[i])**length # adding each powered digit to the result to compare it to the original
    if result==int(num):
        return "Armstrong"
    else:
        return "Not Armstrong"
    
def main():
    input_num=str(input("Enter a number to check :" ))
    result=check_armstrong(input_num)
    print(result)

if __name__=="__main__":
    main()