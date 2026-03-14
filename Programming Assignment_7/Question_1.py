# 1. Write a Python Program to find sum of array?
def sum_array(num_list)->int:
  result=0
  for num in num_list:
    result+=num
  return result

def main():
  try:
        input_list:list=[]
        print("Enter a value below to find sum:")
        while True:
            input_list.append(int(input("- ")))
  except:
        result=sum_array(input_list)
        print(f"Sum is {result}")

if __name__=="__main__":
  main()