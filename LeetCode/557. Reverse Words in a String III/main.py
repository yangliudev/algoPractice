"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""

from typing import List

s = "Let's take LeetCode contest"

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []
        startIndex = 0
        for i in range(len(s)):
            if s[i] == " ":
                endIndex = i
                arr.append(s[startIndex:endIndex])
                startIndex = endIndex + 1
        arr.append(s[startIndex:])
        for i in range(len(arr)):
            arr[i] = arr[i][::-1]
        return " ".join(arr)


#print(s[::-1])
print(Solution().reverseWords(s))