# Write a Python program to print all disarium numbers between 1 to 100?
def is_disarium(num):
    str_num = str(num)    
    disarium_sum = sum(int(digit) ** (index + 1) for index, digit in enumerate(str_num))
    return disarium_sum == num

if __name__ == "__main__":
    for number in range(1, 101):
        if is_disarium(number):
            print(f"{number} is a Disarium number.")
        else:
            print(f"{number} is not a Disarium number.")