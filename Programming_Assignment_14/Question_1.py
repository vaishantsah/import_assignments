class Generator:
    def __init__(self,n):
        self.n = n
    
    def generator(self,):
        for i in range(0,(self.n+1)):
            if(i%7 == 0):
                yield i

if __name__ == "__main__":
    n =int(input("Enter the value of n:"))
    gen=Generator(n)
    for i in gen.generator():
        print(i)