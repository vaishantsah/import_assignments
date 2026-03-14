# Write a Python program to find largest number in a list?

class LargestInList:
    def largest_in_list(x:list)->int:
        largest=x[0]
        for index, value in enumerate(x):
            if value>largest:
                largest=value
        return largest
    
if __name__ == "__main__":
    x:list = [10,2,3,4,5]
    print(f"Largest = {LargestInList.largest_in_list(x)}")