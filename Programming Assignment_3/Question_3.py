def is_leap_year(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  else:
    return False

def main():
  input_year=int(input("Enter an year to check : "))
  result=is_leap_year(input_year)
  if result == True:
    print("Leap Year")
  else:
    print("False")

if __name__=="__main__":
  main()