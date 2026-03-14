#3. Write a Python Program to Print the Fibonacci sequence?
def fibo(num):
  first=0 
  second=1 
  temp=0 
  print(f"{first} ", end="")
  for i in range(0,num):
    print(f"{second} ", end="")
    temp=first+second
    first=second 
    second=temp 

def main():
  input_num=int(input("Enter total Fibonnaci numbers to print : "))
  if input_num<1: 
    print("Enter a positive number")
  else:
    fibo(input_num) 

if __name__=="__main__":
  main()