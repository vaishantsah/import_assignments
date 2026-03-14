# Write a Python program to print even numbers in a list?

class EvenInList:
    def even_in_list(x:list)->list:
        even_in_list=[]
        for index, value in enumerate(x):
            if value%2==0:
                even_in_list.append(value)
        return even_in_list
    
if __name__ == "__main__":
    x:list = [10,2,3,4,5]
    print(f"Even Numbers = {EvenInList.even_in_list(x)}")