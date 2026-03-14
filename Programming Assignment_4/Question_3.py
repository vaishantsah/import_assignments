#3. Write a Python Program to Print the Fibonacci sequence?
def fibo(num):
  first=0 # stores the first number
  second=1 # stores the second number
  temp=0 # will store the sum to update the second number
  print(f"{first} ", end="")
  for i in range(0,num):
    print(f"{second} ", end="")
    temp=first+second
    first=second # update the first number with second number
    second=temp # update the new result in the second number

def main():
  input_num=int(input("Enter total Fibonnaci numbers to print : "))
  if input_num<1: # Cannot be a negative counter
    print("Enter a positive number")
  else:
    fibo(input_num) # Calling the fibo function with counter value

if __name__=="__main__":
  main()