#4. Write a Python Program to Check Prime Number?
def is_prime_num(num):
    counter=0
    if num <0:
        return "Please enter a positive number"
    for i in range(1,num+1):
        if num%i==0:
            counter+=1 #If the number is divisible by i then increase the counter by 1
    if counter==2:
        return True # A Prime number will only get divided twice
    else:
        return False # A Non Prime Number will get divided more or less than 2
def main():
  input_num=int(input("Enter a number to check : "))
  result=is_prime_num(input_num)
  if result == True:
    print("Prime Number")
  elif result == False:
    print("Non Prime Number")
  else:
    print(result)

if __name__=="__main__":
  main()