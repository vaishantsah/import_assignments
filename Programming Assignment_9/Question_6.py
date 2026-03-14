# Write a Python program to print all pronic numbers between 1 and 100?
class Solution(object):
    def is_prontic(self, num:int)->bool:
        """
        :type num: int
        :rtype: bool
        """
        return self.calculate_pronic(num)
    
    def calculate_pronic(self, num:int)->bool:
        for i in range(int(num**0.5) + 1):
            if i * (i + 1) == num:
                return True
        return False

if __name__ == "__main__":
    solution = Solution()
    for n in range(1, 101):
        if solution.is_prontic(n):
            print(f"{n} is a Pronic Number.")
        else:
            print(f"{n} is not a Pronic Number.")