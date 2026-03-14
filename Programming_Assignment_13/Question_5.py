class Strandint_calc:
    def __init__(self,input_string:str)->None:
        self.input_string=input_string

    def calculate_strandint(self)->str:
        count_int=0
        count_str=0
        for val in self.input_string:
            if val.isdigit():
                count_int+=1
            elif val.isalpha():
                count_str+=1
            else:
                pass
        return f"Strings: {count_str} \nIntegers: {count_int}"
    
if __name__ == "__main__":
    input_string=input("Enter a sentence: ")
    calculator=Strandint_calc(input_string)
    result=calculator.calculate_strandint()
    print(result)