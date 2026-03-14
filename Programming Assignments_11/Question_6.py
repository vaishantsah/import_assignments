# Write a Python to find all duplicate characters in string?
class DuplicateCharacters:
    def find_duplicate_characters(string:str)->set:
        char_count = {}
        duplicates = set()

        for char in string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        for char, count in char_count.items():
            if count > 1:
                duplicates.add(char)

        return duplicates
    
if __name__ == "__main__":
    string = "programming"
    result = DuplicateCharacters.find_duplicate_characters(string)
    print(f"Duplicate characters in '{string}': {result}")