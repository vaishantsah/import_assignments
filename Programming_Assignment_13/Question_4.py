class CommaSeperatorAlphaSorter:
    def sort_and_print(self, input_string:str)->str:
        values=input_string.rsplit(' ')
        value=set(values)
        value=sorted(value)
        return ' '.join(value)

if __name__ == "__main__":
    input_string=input("Enter values with space seperation: ")
    sorter=CommaSeperatorAlphaSorter()
    result=sorter.sort_and_print(input_string)
    print(f"Sorted Values are : {result}")