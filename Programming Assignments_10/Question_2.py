# Write a Python program to Multiply all numbers in the list?
class MultiplyList:

    def multiply_list(x:list)->list:
        if len(x)==0:
            return 0
        else:
            result=1
            for index, value in enumerate(x):
                result*=value
            return result
        
if __name__ == "__main__":
    x:list = [1,2,3,4,5]
    print(f"Multiplication = {MultiplyList.multiply_list(x)}")