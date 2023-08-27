# Find if there exists a palindrome of length n from given s

def findPalindrome(s, n):
    for i in range(len(s)):
        word = s[i:i+n]
        if word == word[::-1]:
            return i
    
    return -1

print(findPalindrome('ABBAbcd', 4)) # returns 0
print(findPalindrome('Helloworld wowowow', 3)) # returns 4
