# Write a Python to check if a given string is binary string or not?

class stringBinary:
    def check_binary(string:str)->bool:
        for char in string:
            if char == '0' or char == '1':
                continue
            else:
                return False

if __name__=="__main__":
    string="101010101010"
    print(f"Given String: {string}")
    value = stringBinary.check_binary(string)
    if value==None or value==True:
        print(f"Is Binary")
    else:
        print(f"Not a Binary")