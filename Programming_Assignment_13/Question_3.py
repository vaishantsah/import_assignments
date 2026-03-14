class CommasSeperatedSorter:
    def sort_comma_sep_values(self, input_string:str)->str:
        values=input_string.rsplit(',')
        values.sort()
        return ','.join(values)
    
if __name__ == "__main__":
    input_string=input("Enter values with comma seperation: ")
    sorter=CommasSeperatedSorter()
    result=sorter.sort_comma_sep_values(input_string)
    print(f"Sorted Values are : {result}")