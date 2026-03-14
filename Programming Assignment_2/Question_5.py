# Write a Python program to swap two variables without temp variable?
def swap(var1,var2):
  x=var1
  y=var2
  x=x+y
  y=x-y #y is now x
  x=x-y #x is now y
  return x,y

def main():
  variable1=int(input("Enter first variable "))
  variable2=int(input("Enter second variable "))
  print(f"Variable 1 is {variable1}\nVariable 2 is {variable2}")
  result1, result2 = swap(variable1, variable2)
  print(f"Variable 1 now is {result1}\nVariable 2 now is {result2}")

if __name__=="__main__":
  main()