#2. Write a Python Program to Display the multiplication Table?
def print_table(num):
  for i in range(1,11):
    result=num*i  
    print(f"{num} x {i} = {result}")

def main():
  input_num=int(input("Enter an integer - "))
  print_table(input_num)

if __name__=="__main__":
  main()