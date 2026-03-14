# 4. Write a Python Program To Find ASCII value of a character?
def is_ascii(input_value):
    return(ord(input_value))

def main():
    key=input("Enter a key : ")
    print(is_ascii(key))

if __name__=="__main__":
    main()