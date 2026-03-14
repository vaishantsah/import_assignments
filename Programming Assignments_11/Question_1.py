# Write a Python program to find words which are greater than given length k?

class FindWordsGreaterThanK:
    def greater_than(words:list,k:int)->list:
        return [word for word in words if len(word)>k]
    
if __name__ == "__main__":
    words=["ineuron","data","science","machine","learning","artificial","intelligence"]
    k=5
    print(f"Words greater than length {k}: {FindWordsGreaterThanK.greater_than(words,k)}")