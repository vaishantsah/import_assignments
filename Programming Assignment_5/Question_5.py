# 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
def add(first,second)->int:
    return first+second

def sub(first, second)->int:
    return first-second

def mul(first,second)->float:
    return first*second

def div(first,second)->float:
    try:
        return first/second
    except ZeroDivisionError as e:
        return "Cannot divide by zero"
    except Exception as e:
        return f"{e}"
    
def main():
    print("1. Add \n2. Subtract\n3. Multiply\n4. Divide\nChoose a number for operation")
    choice=int(input())
    if choice==1:
        try:
            add_first=int(input("First number : "))
            add_second=int(input("Second input : "))
            print(add(add_first,add_second))
        except Exception as e:
            print(e)
    elif choice==2:
        sub_first=int(input("First number : "))
        sub_second=int(input("Second input : "))
        print(sub(sub_first,sub_second))
    elif choice==3:
        mul_first=float(input("First number : "))
        mul_second=float(input("Second number : "))
        print(mul(mul_first,mul_second))
    elif choice==4:
        div_first=float(input("First number : "))
        div_second=float(input("Second number :"))
        print(div(div_first,div_second))
    else:
        print("Please enter correct choice values")

if __name__=="__main__":
    main()