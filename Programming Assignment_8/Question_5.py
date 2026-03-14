# Write a Python Program to Remove Punctuation From a String
import string

def remove_punctuation(sentence)->str:
    translator=str.maketrans('','',string.punctuation)
    clean_text=sentence.translate(translator)
    return clean_text

if __name__ == "__main__":
    sentence:str="Hello, world! How do this work? zz'' after all."
    result:str=remove_punctuation(sentence)
    print("Removing punctuation from the following sentence below")
    print(f"Sentence: {sentence}")
    print(f"Cleaned Sentence: {result}")