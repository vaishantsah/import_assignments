class Sentence:
    def __init__(self, sentence:str):
        self.sentence:str = sentence

    def get_sentence(self):
        my_dict={}
        words=self.sentence.split(' ')
        for word in words:
            count=self.sentence.count(word)
            my_dict[word]=count
        sorted_dict= dict(sorted(my_dict.items()))
        for key,values in sorted_dict.items():
            print(f"{key} : {values}")

if __name__ == "__main__":
    sentence_input = input("Enter a sentence: ")
    sentence_obj = Sentence(sentence_input)
    sentence_obj.get_sentence()