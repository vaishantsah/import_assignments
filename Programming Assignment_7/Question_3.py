# 3. Write a Python Program for array rotation?
def right_rotate_array(num:list,position:int)->list:
    
    k=position%len(num)
    l,r=0,len(num)-1
    while l<r: #using the mod to first rotate the array
        num[l], num[r] = num[r], num[l]
        l, r=l+1,r-1
    
    l, r=0,position-1
    while l<r: # loop to reverse the first part of array
        num[l], num[r] = num[r], num[l]
        l, r=l+1,r-1
    
    l, r=k, len(num)-1
    while l<r: # loop to rotate the second part of array
        num[l], num[r] = num[r], num[l]
        l, r=l+1,r-1
    return num

def main():
    pos=int(input("Enter the position to shift : "))
    try:
        input_list:list=[]
        print("Enter a value below to rotate:")
        while True:
            input_list.append(int(input("- ")))
    except:
        result:list=right_rotate_array(input_list,pos)
        print(f"New array is {result}")

if __name__=="__main__":
    main()