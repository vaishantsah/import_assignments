# Write a Python program to Extract Unique values dictionary values?

class UniqueValuesExtractor:
    def extract_unique_values(input_dict:dict)->list:
        unique_values=set()
        for value in input_dict.values():
            unique_values.add(value)
        return list(unique_values)
    
if __name__=="__main__":
    input_dict={'a':1,'b':2,'c':3,'d':2,'e':1}
    print("Input Dictionary:",input_dict)
    result=UniqueValuesExtractor.extract_unique_values(input_dict)
    print("Unique Values:",result)