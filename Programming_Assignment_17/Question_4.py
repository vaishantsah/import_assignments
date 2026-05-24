def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
if __name__=="__main__":
    n=int(input("Enter a number : "))
    print(f"The factorial for {n} is {fact(n)}")
    