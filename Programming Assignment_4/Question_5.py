# 5. Write a Python Program to Find Armstrong Number in an Interval?
def check_armstrong(lower,upper):
    for num in range(lower,upper+1):
        power=len(str(num))
        result=0
        copy_num=num
        while copy_num>0:
            digit=copy_num%10
            result+=(digit**power)
            copy_num=copy_num//10
        if result==num:
            print(f"{num} is Armstrong Number")
        else:
            print(f"{num} is not an Armstrong number")

def main():
    low=int(input("Enter the lower range : "))
    high=int(input("Enter the higher range : "))
    if high<low:
        print("Enter a higher range")
    else:
        print(check_armstrong(low,high))

if __name__=="__main__":
    main()