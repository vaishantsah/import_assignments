# Write a Python program to convert key-values list to flat dictionary?

class FlatDictionaryConverter:
    def convert_dict(book:list)->dict:
        flat_dict={}
        flat_dict=dict(book)
        return flat_dict
    
if __name__=="__main__":
    book=[('name','apple'),('color','red'),('price',100)]
    result=FlatDictionaryConverter.convert_dict(book)
    print(result)