# Write a Python Program to Sort Words in Alphabetic Order?

def sort_alphabetically(sentence):
    words:list=sentence.split()
    words.sort(key=str.lower)
    print(words)
    result=""
    for word in words:
        result=result+word+" "
    return result

if __name__ == "__main__":
    sentence:str="Hello world how do this work zz after all"
    result=sort_alphabetically(sentence)
    print("Sorting the following sentence below")
    print(f"Sentence: {sentence}")
    print(f"Sorted Sentence: {result}")