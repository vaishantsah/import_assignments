# 7. Write a Python Program to check if a string contains any special character?
import string

class SpecialChar:
    def contains_special_char(sentence:str)->bool:
        for char in sentence:
            if char in string.punctuation:
                return True
    
if __name__=="__main__":
    sentence="Hello@World"
    result=SpecialChar.contains_special_char(sentence)
    if result:
        print(f"The string '{sentence}' contains special characters.")
    else:
        print(f"The string '{sentence}' does not contain any special characters.")