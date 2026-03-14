# 2. Write a Python Program to find largest element in an array?
def largest_array(num_list):
  chosen=num_list[0]
  for num in num_list:
    if num>chosen:
      chosen=num
  return chosen

def main():
  try:
        input_list:list=[]
        print("Enter a value below to find largest:")
        while True:
            input_list.append(int(input("- ")))
  except:
        result=largest_array(input_list)
        print(f"Largest is {result}")

if __name__=="__main__":
  main()