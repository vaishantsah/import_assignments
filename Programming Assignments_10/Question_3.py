# Write a Python program to find smallest number in a list?

class SmallestInList:
    def smallest_in_list(x:list)->int:
        smallest=x[0]
        for index, value in enumerate(x):
            if value<smallest:
                smallest=value
        return smallest
    
if __name__ == "__main__":
    x:list = [10,2,3,4,5]
    print(f"Smallest = {SmallestInList.smallest_in_list(x)}")