# Write a Python program to Remove empty List from List?

class RemoveEmptyList:
    def remove_empty_list(x:list)->list:
        return [i for i in x if i] #if i is not empty return True in case of empty it returns False

if __name__ == "__main__":
    x=[5,6,[],3,[],[],9]
    print(f"Original List: {x}")
    print(f"List after removing empty lists: {RemoveEmptyList.remove_empty_list(x)}")