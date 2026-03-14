#1. Write a Python Program to Find LCM?
import math
def find_lcm(num_list):
    return(math.lcm(*num_list))

def main():
    try:
        input_list:list=[]
        print("Enter a value below to find LCM:")
        while True:
            input_list.append(int(input("- ")))
    except:
        result=find_lcm(input_list)
        print(f"LCM is {result}")

if __name__=="__main__":
    main()