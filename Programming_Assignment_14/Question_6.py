# Please write a binary search function which searches an item in a sorted list. The
# function should return the index of element to be searched in the list.
class BinarySearch:
    def __init__(self, sorted_list:list, target:int)->None:
        self.target = target
        self.sorted_list = sorted_list

    def binary_search(self)->int:
        arr = self.sorted_list
        target = self.target
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        
if __name__=="__main__":
    sorted_list=[1,3,5,7,9,11,13,15,17,19]
    target=7
    searcher=BinarySearch(sorted_list, target)
    result=searcher.binary_search()
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the list.")
            