class EvelyDistributed:
    def __init__(self, first:int, last:int, divisor:int):
        self.first=first
        self.last=last
        self.divisor=divisor
        
    def evenly_distributed(self):
        if self.first > self.last:
            return "First number should be less than or equal to last number."
        if self.divisor == 0:
            return "Divisor cannot be zero."
        
        result = 0
        for num in range(self.first, self.last + 1):
            if num % self.divisor == 0:
                result += num
        return result
    
if __name__=="__main__":
    first = int(input("Enter the first number: "))
    last = int(input("Enter the last number: "))
    divisor = int(input("Enter the divisor: "))
    
    even_dist = EvelyDistributed(first, last, divisor)
    result = even_dist.evenly_distributed()
    print(f"The sum of numbers between {first} and {last} that are evenly divisible by {divisor} is: {result}")