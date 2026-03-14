# 4. Write a Python Program to Split the array and add the first part to the end?
def split_array(num:list,position:int)->list:
    first_list=[]
    second_list=[]
    l,r=0,position
    while l<r:
        first_list.append(num[l])
        l+=1
    
    l,r=position, len(num)-1
    while l<r:
        second_list.append(num[l])
        l+=1
    
    return first_list,second_list

def add_list(first:list,second:list)->list:
    for i in range(0,len(first)):
        second.append(first[i])
    return second

def main():
    position=int(input("Enter position : "))
    first_list=[]
    print("Enter values belows for list:")
    try:
        while True:
            input_value=int(input("-"))
            first_list.append(input_value)
    except:
        first,second=split_array(first_list,position)
        result=add_list(first,second)
        print(result)

if __name__=="__main__":
    main()