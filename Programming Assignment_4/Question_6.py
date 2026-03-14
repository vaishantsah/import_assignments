#6. Write a Python Program to Find the Sum of Natural Numbers?
from functools import cache

@cache
def natural_sum(num:int):
  result=0
  for i in range(0,num+1):
    result+=i
  return result

def main():
  input_range=int(input("Enter a range end : "))
  result=natural_sum(input_range)
  print(f"The sum of natural numbers till {input_range} is {result}")

if __name__=="__main__":
  main()