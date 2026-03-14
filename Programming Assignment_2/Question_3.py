# Write a Python program to display calendar?
import calendar
def display_calendar(month,year)->calendar.month:
  return calendar.month(year,month)

def main():
  month=int(input("Enter month "))
  year=int(input("Enter year "))
  print(f"=="*10)
  result=display_calendar(month,year)
  print(result)

if __name__=="__main__":
  main()