class BinaryConvertor:
    def __init__(self,num):
        self.num = num
    
    def convert_to_binary(self):
        binary = bin(self.num)
        return binary[2:]
    
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    convertor = BinaryConvertor(num)
    print(f"{num} = {convertor.convert_to_binary()}")