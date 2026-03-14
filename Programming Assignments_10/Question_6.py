# Write a Python program to find N largest elements from a list?

class NLargestInList:
    def n_largest(x:list, n:int)->list:
        x=sorted(set(x),reverse=True)
        return x[:n]

if __name__ == "__main__":
    x:list = [10,2,81,4,5,10,3]
    n:int = 3
    print(f"{n} Largest = {NLargestInList.n_largest(x,n)}")