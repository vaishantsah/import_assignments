vowels="aeiou"

def replace_vowels(sentence:str, character:str)->str:
    for char in sentence:
        if char.lower() in vowels:
            sentence = sentence.replace(char, character)
    return sentence

if __name__=="__main__":
    sentence=input("Enter a sentence: ")
    print(replace_vowels(sentence, "#"))