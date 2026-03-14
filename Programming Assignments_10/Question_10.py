# Write a Python program to Cloning or Copying a list?

class CloneList:
    def clone_list(x:list)->list:
        return(x[:])

if __name__ == "__main__":
    x=[1,2,3,4,5]
    b=[5,6,7,8,9]
    print(f"Original List: {x}")
    print(f"Another List: {b}")
    b= CloneList.clone_list(x)
    print(f"Cloned List: {b}")