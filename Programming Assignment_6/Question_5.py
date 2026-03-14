# 5. Write a Python Program for cube sum of first n natural numbers?
def cube_sum(limit):
    for num in range(1,limit+1):
        mid_value=num+1
        mid_value*=mid_value
        print(((num*num)*mid_value)/4)

def main():
    input_value=int(input("Enter limit : "))
    print(cube_sum(input_value))

if __name__=="__main__":
    main()