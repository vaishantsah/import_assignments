# Write a Python program to determine whether the given number is a Harshad Number?
class Solution(object):
    def is_harshad(self,num)->True:
        """
        :type num: int
        :rtype: bool
        """
        return self.calculate_harshad(num)
    
    def calculate_harshad(self, num:int)->bool:
        digit_sum = sum(int(digit) for digit in str(num))
        flag= num % digit_sum
        if flag == 0:
            return True
        else:
            return False
        
if __name__=="__main__":
    number = int(input("Enter a number: "))
    solution = Solution()
    if solution.is_harshad(number):
        print(f"{number} is a Harshad number.")
    else:
        print(f"{number} is not a Harshad number.")