# Write a Python program to check if the given number is Happy Number?
class Solution(object):
    def isHappy(self, n:int)->bool:
        """
        :type n: int
        :rtype: bool
        """
        visit=set()
        while n not in visit:
            visit.add(n)
            n=self.sumOfSquares(n)
            if n==1:
                return True
        return False

    def sumOfSquares(self, n:int)->int:
        sum=0
        while n:
            digit=n%10
            sum+=digit**2
            n=n//10
        return sum
    
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    solution = Solution()
    if solution.isHappy(n):
        print(f"{n} is a Happy Number.")
    else:
        print(f"{n} is not a Happy Number.")