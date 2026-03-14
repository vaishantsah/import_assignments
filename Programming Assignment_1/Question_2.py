def add(*nums):
    result=0
    numbers=nums
    for num in numbers:
        result+=num
    return result

def div(num1:int,num2:int):
    try:
        result=num1//num2
        return result
    except ZeroDivisionError as zero:
        return f"Cannot perform {zero}"
    except Exception as e:
        return f"Error occured {e}"
    
def main():
    num_list:list=()
    num_list=input("Enter a list of numbers to add (seperated by commas): ")
    num_list=[int(num) for num in num_list.split(",")]
    adding=add(*num_list)
    print(f"Addition result {adding}")
    division=div(4,1)
    print(f"Division result {division}")

if __name__=="__main__":
    main()