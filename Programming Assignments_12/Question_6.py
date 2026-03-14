# Write a Python program to check order of character in string using OrderedDict()?
from collections import OrderedDict

class CharacterOrderChecker:

    def __init__(self,main_string, pattern):
        self.main_string = main_string
        self.pattern= pattern

    def check_order(self,)->bool:
        od=OrderedDict.fromkeys(self.main_string)
        ptr=0
        for char_in_string in od:
            if ptr < len(self.pattern) and char_in_string == self.pattern[ptr]:
                ptr+=1
        return ptr==len(self.pattern)
    
if __name__ == "__main__":
    main_string = "engineers rock"
    pattern = "er"
    checker = CharacterOrderChecker(main_string, pattern)
    result = checker.check_order()
    print(f"The pattern '{pattern}' appear in order in the string '{main_string}'? \n{result}")