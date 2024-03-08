# your code goes here
class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        matches = []
        for word in word_list:
            if sorted(word) == sorted(self.word) and word != self.word:
                matches.append(word)
        return matches