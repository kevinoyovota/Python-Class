# word2 if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        word1_list = list(word1.lower())
        word2_list = list(word2.lower())

        if sorted(word1_list) != sorted(word2_list):
            return False

    return True


word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

print(find_anagrams(word1, word2))

