#Returns all duplicate chars in a str

strs = "hello"

def printDup(strs):

    dic = {}
    for i in strs:
        dic[i] = dic.get(i, 0) + 1

    for i in dic:
        if dic[i] > 1:
            return i

# print(printDup(strs))

#Check if 2 strs are anagrams of each other

#One problem with this implementation is what if theres non alphanumeric characters?

strs1 = 'School master'
strs2 = 'The classroom'

def checkAnagram(strs1, strs2):
    #convert to case insensitive
    low1 = strs1.lower()
    low2 = strs2.lower()

    #Put string in list
    listy1 = list(low1)
    listy2 = list(low2)
        
    # print(sorted(listy1))
    # print(sorted(listy2))

    if sorted(listy1) == sorted(listy2):
        return True
    else:
        return False

#print(checkAnagram(strs1, strs2))

#print the first non-repeated character from a string
strs3 = 'aaabccd'

def nonRepeatChar(strs3):
    dic = {}
    for i in strs3:
        dic[i] = dic.get(i, 0) + 1

    for i in dic:
        if dic[i] == 1:
            return i

#print(nonRepeatChar(strs3))

#count vowels and consonants in a str
strs4 = 'aeioubc'

def countVowelConsonant(strs4):

    vowels = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }

    vowel_count = 0
    consonant_count = 0
    
    for i in range(len(strs4)):
        if strs4[i] in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

    print(vowel_count)
    print(consonant_count)

print(countVowelConsonant(strs4))

#Reverse a string
strs5 = 'hello'
print(strs5[::-1])

#Reverse a string without string slicing
strs5 = 'hello'
listy5 = list(strs5)
listy5.reverse()
print(''.join(listy5))

#Generate all permutations of a string
str6 = 'abc'
fact = 1
for i in range(1, len(str6) + 1):
    fact = fact * i

print(fact)