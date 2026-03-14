# 2. Write a Python Program to Find HCF?
import math
def find_lcm(num_list):
    return(math.gcd(*num_list))

def main():
    try:
        input_list:list=[]
        print("Enter a value below to find HCF :")
        while True:
            input_list.append(int(input("- ")))
    except:
        result=find_lcm(input_list)
        print(f"HCF is {result}")

if __name__=="__main__":
    main()