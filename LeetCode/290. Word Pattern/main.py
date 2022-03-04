pattern = "abba"
strs = "dog cat cat dog"

class Solution:
    def wordPattern(self, pattern: str, strs: str) -> bool:
        dic = {}
        arr = []

        startIndex = 0
        for i in range(len(strs)):
            if strs[i] == ' ':
                arr.append(strs[startIndex:i])
                startIndex = i+1
        arr.append(strs[startIndex:])

        for i in range(len(arr)):
            for j in range(len(pattern)):
                if i > 0:
                    j = i
                dic[pattern[j]] = arr[i]

        print(dic)

print(Solution().wordPattern(pattern, strs))