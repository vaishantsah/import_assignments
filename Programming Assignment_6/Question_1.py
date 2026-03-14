def fibonacci(n):
    if n <= 0:
        return "Invalid input. The input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def print_fibonacci_series(n):
    if n <= 0:
        print("Please enter a positive number")
    else:
        print("Fibonacci Series:")
        for i in range(1, n + 1):
            print(fibonacci(i), end=" ")

def main():
    terms=int(input("Enter the number of fibonacci numbers : "))
    print(print_fibonacci_series(terms))

if __name__=="__main__":
    main()