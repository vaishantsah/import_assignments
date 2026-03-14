# C is 50. H is 30.
# formula = [(2*C*D)/H]

import math

def calculate_value(x)->int:
    C=50
    H=30
    value=(2*C*x)/H
    if value<0:
        return 0
    else:
        return math.sqrt(value)
    
def main():
    values=input("Enter the values of D separated by comma: ")
    value=values.rsplit(',')
    for i in range(len(value)):
        print(f"The result for D={value[i]} is : {int(calculate_value(int(value[i])))}")

if __name__ == "__main__":
    main()