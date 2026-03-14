# Write a Python program to find second largest number in a list?

class SecodndLargestInList:
    def second_largest(x:list)->int:
        x=sorted(set(x),reverse=True)
        return x[1]
    
if __name__ == "__main__":
    x:list = [10,2,3,4,5,10,3]
    print(f"Second Largest = {SecodndLargestInList.second_largest(x)}")