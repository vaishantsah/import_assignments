# Write a Python program to Merging two Dictionaries?
class MergeDictionaries:
    def merge_dicts(dict1:dict,dict2:dict)->dict:
        merge_dictionary= dict1 | dict2
        return merge_dictionary

if __name__=="__main__":
    dict1={'a':1,'b':2,'c':3}
    dict2={'c':4,'e':5,'f':6}
    print("First Dictionary:",dict1)
    print("Second Dictionary:",dict2)
    result=MergeDictionaries.merge_dicts(dict1,dict2)
    print("Merged Dictionary:",result)