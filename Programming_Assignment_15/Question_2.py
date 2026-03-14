class Generator:
    def __init__(self, n:int)->None:
        self.max:int=n

    def yield_num(self):
        for i in range(0,self.max+1):
            if i%2==0:
                yield i
    
if __name__=="__main__":
    n=int(input("Enter the maximum number: "))
    generate=Generator(n)
    numbers=generate.yield_num()
    for n in numbers:
        print(f"{n}",end=",")