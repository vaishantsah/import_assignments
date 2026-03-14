# Write a Python program to sort Python Dictionaries by Key or Value?
class DictionarySorter:
    def __init__(self, input_dict:dict):
        self.diction=input_dict
    
    def sort_by_key(self,)->dict:
        diction_by_key = dict(sorted(self.diction.items()))
        print("Dictionary sorted by key:", diction_by_key)
    
    def sort_by_value(self,)->dict:
        diction_by_value = dict(sorted(diction.items(), key=lambda item: item[1]))
        print("Dictionary sorted by value:", diction_by_value)

if __name__=="__main__":
    diction = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
    print("Original Dictionary:", diction)
    sorter = DictionarySorter(diction)
    sorter.sort_by_key()
    sorter.sort_by_value()