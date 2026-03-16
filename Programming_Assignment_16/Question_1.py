class Stutter:
    def __init__(self,word:str):
        self.word=word
    
    def stutter(self)->str:
        if len(self.word)<2:
            return "Too short"
        else:
            stutter_word=self.word[:2]
            return f"{stutter_word}... {stutter_word}... {self.word}?"
        
if __name__=="__main__":
    word=str(input("Enter a word: "))
    stutter=Stutter(word)
    print(stutter.stutter())