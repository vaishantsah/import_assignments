# Write a Python program for removing i-th character from a string?
class RemoveIthCharacter:
    def remove_char(sentence:str,i:int)->str:
        return sentence[:i]+sentence[i+1:]
    
if __name__=="__main__":
    sentence = "ineuron"
    i = 3
    print(f"Original String: {sentence}")
    print(f"Removing i-th char :{RemoveIthCharacter.remove_char(sentence,i)}")