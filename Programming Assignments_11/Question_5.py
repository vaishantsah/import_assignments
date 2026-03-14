# Write a Python program to find uncommon words from two Strings?
class UncommonWords:
    def find_uncommon_word(str1:str, str2:str)->list:
        word1 =set(str1.split())
        word2 =set(str2.split())

        result = list(word1 ^ word2)
        return result

if __name__ == "__main__":
    str1 = "Python is a programming language"
    str2 = "Python is used for data science"
    print(UncommonWords.find_uncommon_word(str1, str2))