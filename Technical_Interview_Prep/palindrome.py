#Determine if an integer is a palindrome
#This question is very easy, next challenge is do this but no converting to str

# x = 121
# from typing import List

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if str(x) == str(x)[::-1]:
#             return True
#         else:
#             return False

# print(Solution().isPalindrome(x))

#Given a string, determine if it is a palindrome,
# considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.

class Solution2:
    def isPalindrome(self, s: str) -> bool:
        
        #Check for edge case
        if s == "":
            return True
        
        #Ignore cases
        lower = s.lower()
        print(lower)
        
        #Put string in list
        listy = list(lower)
        print(listy)
        
        #Remove non alphanumeric characters
        i = 0
        while i < len(listy):
            if listy[i].isalnum() != True:
                listy.pop(i)
            else:
                i += 1
        
        if listy == listy[::-1]:
            return True
        else:
            return False

#Determine if a string is a palindrome WITHOUT string slicing or using libraries
pali = "abbbbbbbbba"

def paliDrone(pali):
    i = 0
    j = len(pali) - 1
    while i < j:
        if pali[i] == pali[j]:
            i += 1
            j -= 1
            continue
        else:
            return False
    return True

print(paliDrone(pali))