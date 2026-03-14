# Write a Python program to find sum of elements in list?
class ListSum:
    
    def sum_of_list(x:list)->int:
        return sum(x)

if __name__ == "__main__":
    x:list =[1,2,3,4,5]
    print(f"Sum = {ListSum.sum_of_list(x)}")