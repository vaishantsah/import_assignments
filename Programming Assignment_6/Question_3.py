# 3. Write a Python Program to calculate your Body Mass Index?
def bmi(weight, height):
    height*=height
    try:
        return weight/height
    except ZeroDivisionError as e:
        return e
    except Exception as e:
        return e
    
def main():
    height=float(input("Enter height : "))
    weight=float(input("Enter weight : "))
    print(bmi(weight,height))

if __name__=="__main__":
    main()