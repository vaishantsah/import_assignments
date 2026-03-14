# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
from functools import cache
@cache
def is_prime_range():
  for i in range(1,10001):
    counter=0
    for j in range(1,i+1):
      if i%j==0:
        counter+=1
    if counter==2:
      print(f"{i} is Prime Number")

def main():
  is_prime_range()

if __name__=="__main__":
  main()