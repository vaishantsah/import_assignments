# Write a Python program to find the sum of all items in a dictionary?
class DictionarySumCalculator:
    def sum_of_dict(input_dict:dict)->int:
        sum=0
        for item in input_dict.values():
            sum+=item
        return sum
    
if __name__=="__main__":
    input_dict={'a':1,'b':2,'c':3,'d':4,'e':5}
    print("Input Dictionary:",input_dict)
    result=DictionarySumCalculator.sum_of_dict(input_dict)
    print("Sum of all items in the dictionary:",result)