# Write a Python program to insertion at the beginning in OrderedDict?
from collections import OrderedDict

class OrderedDictInsertion:
    def insert_at_first(dictionaries:dict,key:str,value:int)->OrderedDict:
        od=OrderedDict(dictionaries)
        od.update({key:value})
        od.move_to_end(key,last=False)
        return od

if __name__=="__main__":
    dictionaries={'a':1,'b':2,'c':3}
    key:str='d'
    value:int=4
    print("Original Dictionary:",dictionaries)
    result=OrderedDictInsertion.insert_at_first(dictionaries,key,value)
    print("Dictionary after insertion at the beginning:",result)
