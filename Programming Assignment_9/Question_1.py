# Write a Python program to check if the given number is a Disarium Number?
def is_disarium(num):
    str_num = str(num)    
    disarium_sum = sum(int(digit) ** (index + 1) for index, digit in enumerate(str_num))
    return disarium_sum == num

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if is_disarium(number):
        print(f"{number} is a Disarium number.")
    else:
        print(f"{number} is not a Disarium number.")