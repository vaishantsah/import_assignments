class Fibolistcomp:
    def __init__(self, n):
        self.n = n

    def fibolistcomp(self):
        if self.n < 1:
            return []
        fibolist = [0]
        if self.n >= 2:
            fibolist.append(1)
        [fibolist.append(fibolist[-1] + fibolist[-2]) for i in range(2, self.n)]
        return fibolist

if __name__ == "__main__":
    n = int(input("Enter total Fibonacci numbers to print: "))
    if n < 1:
        print("Enter a positive number")
    else:
        fibolistcomp = Fibolistcomp(n)
        print(','.join(map(str, fibolistcomp.fibolistcomp())))