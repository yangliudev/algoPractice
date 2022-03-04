from typing import List

words = ["Hello", "Alaska", "Dad", "Peace"]

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set('qwertyuiopQWERTYUIOP')
        second_row = set('asdfghjklASDFGHJKL')
        third_row = set('zxcvbnmZXCVBNM')
        arr = []
        for i in range(len(words)):
            if set(words[i]).intersection(first_row) == set(words[i]):
                arr.append(words[i])
            elif set(words[i]).intersection(second_row) == set(words[i]):
                arr.append(words[i])
            elif set(words[i]).intersection(third_row) == set(words[i]):
                arr.append(words[i])
        return arr

print(Solution().findWords(words))