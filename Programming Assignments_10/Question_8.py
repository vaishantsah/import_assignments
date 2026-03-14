# Write a Python program to print odd numbers in a List?

class OddInList:
    def odd_in_list(x:list)->list:
        odd_in_list=[]
        for index, value in enumerate(x):
            if value%2!=0:
                odd_in_list.append(value)
        return odd_in_list

if __name__ == "__main__":
    x:list = [1,2,3,4,5]
    print(f"Odd Numbers = {OddInList.odd_in_list(x)}")