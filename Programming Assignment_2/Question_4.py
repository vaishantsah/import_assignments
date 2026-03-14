# Write a Python program to solve quadratic equation?
import math
import cmath

def quad_equation(a,b,c):
  if a==0:
    return "First coefficient cannot be 0"
  else:
    discriminant=(b**2)-(4*a*c)
    if discriminant < 0: 
        positive=(-b+cmath.sqrt(discriminant))/(2*a)
        negative=(-b-cmath.sqrt(discriminant))/(2*a)
        return positive, negative
    
    else :
        positive=(-b+math.sqrt(discriminant))/(2*a)
        negative=(-b-math.sqrt(discriminant))/(2*a)
        return positive, negative

def main():
  print("The convention to follow quadratic equation is : ax2 + bx + c=0")
  x=int(input("Enter first coefficient(a) "))
  y=int(input("Enter second coefficient(b) "))
  c=int(input("Enter third coefficient(c) "))
  positive,negative=quad_equation(x,y,c)
  if isinstance(positive,complex) or isinstance(negative,complex):
    print(f"Root 1 ={positive.real} + {positive.imag}j\nRoot 2 ={negative.real} + {negative.imag}j")
  else:
    print(f"Root 1 ={positive}\nRoot 2 ={negative}")

if __name__=="__main__":
  main()