# Write a Python program to Count occurrences of an element in a list?

class CountOccurrences:
    def count_occur(x:list,element:int)->int:
        return x.count(element)
    
if __name__ == "__main__":
    x=[1,2,3,4,5,1,2,1,1]
    element=1
    print(f"List: {x}")
    print(f"Element to count: {element}")
    print(f"Occurrences of {element} in list: {CountOccurrences.count_occur(x,element)}")