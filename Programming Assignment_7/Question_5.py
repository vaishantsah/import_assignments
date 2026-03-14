# 5. Write a Python Program to check if given array is Monotonic?
def decreasing_monotonic(nums:list)->str:
    global flag
    flag=0
    for i in range(0,len(nums)-1):
        if nums[i]>nums[i+1]:
            flag=1
            return "Non monotonic"
    if flag==0:
        return "Increasing Monotonic"
    
def increasing_monotonic(nums:list)->str:
    global flag
    flag=0
    for i in range(0,len(nums)-1):
        if nums[i]<nums[i+1]:
            flag=1
            return "Non monotonic"
    if flag==0:
        return "Decreasing Monotonic"
            
def main():
    try:
        input_list:list=[]
        print("Enter a value below to find a monotonic list:")
        while True:
            input_list.append(int(input("- ")))
    except:
        if input_list[0]<input_list[1] or input_list[0]==input_list[1]:
            result=decreasing_monotonic(input_list)
            print(f"List is {result}")
        elif input_list[0]>input_list[1] or input_list[0]==input_list[1]:
            result=increasing_monotonic(input_list)
            print(f"List is {result}")
        else:
            print("Non monotonic")
            
if __name__=="__main__":
  main()