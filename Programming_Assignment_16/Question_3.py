class Curzon:
    def __init__(self, num:int):
        self.num=num
    def calculate(self)->bool:
        if (1+2**self.num)%(1+2*self.num)==0:
            return True
        else:
            return False

if __name__=="__main__":
    num=int(input("Enter a number: "))
    curzon=Curzon(num)
    print(curzon.calculate())