# Write a Python program to split and join a string?
class SplitandJoin:
        def split_join_string(sentence:str,splitter:str)->str:
            split_string=sentence.split(splitter)
            print(f"String after split: {split_string}")
            return " ".join(split_string)
        
if __name__=="__main__":
    sentence = "Ineuron Full Stack Data Science"
    splitter=" "
    print(f"Original String: {sentence}")
    print(f"String after split and join: {SplitandJoin.split_join_string(sentence,splitter)}")