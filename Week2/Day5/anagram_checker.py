import itertools as iter

class AnagramChecker:
    def __init__(self):
        with open(r'C:\Users\User\Documents\DI-Bootcamp\Week2\Day5\sowpods.txt', 'r', encoding='utf-8') as file:
            self.words = [line.strip().lower() for line in file.readlines()]  # Convert words to lowercase

    def is_valid_word(self, words):
        return words.lower() in self.words

    def get_anagrams(self, words):
        if not self.is_valid_word(words):
            raise ValueError(f"The word '{words}' is not in the word list.")
        
        words = words.lower()
        find_anagram = set(''.join(perm) for perm in iter.permutations(words))  # Use itertools to permute the word and find anagrams
        anagrams = []
        for i in self.words:
            if i in find_anagram and i != words:
                anagrams.append(i)
        return anagrams

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

test = AnagramChecker()

print(test.is_valid_word('meat'))

   