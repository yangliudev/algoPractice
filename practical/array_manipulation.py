import math

#Add item to end of an array
arr = [1, 2, 3, 4, 5]

arr.append(6)
print(arr)

#Add item to beginning of an array
arr2 = [1, 2, 3, 4, 5]

arr2.insert(0, 0)
print(arr2)

#Convert an array of strings into a single string
arr3 = ["h", "e", "l", "l", "o"]
print("".join(arr3))

#Convert an array of integers into a single string
arr4 = [1, 2, 3, 4, 5]
str_arr4 = [str(i) for i in arr4]
print(str_arr4)
print("".join(str_arr4))

#Convert a string into a array of strings
strs5 = "hello"
arr5 = []
for i in strs5:
    arr5.append(i)

print(arr5)

#Split string into a list
strs6 = "welcome to the jungle"
print(strs6.split(" "))

#Split string into a list manually (without library)
arr7 = []
strs7 = "hello my dog cute"

startIndex = 0
for i in range(len(strs7)):
    if strs7[i] == ' ':
        arr7.append(strs7[startIndex:i])
        startIndex = i+1
arr7.append(strs7[startIndex:])

print(arr7)

#Add array of integers without using SUM
arr8 = [1, 2, 3, 4, 5]
sums = 0
for i in arr8:
    sums += i
print(sums)

# Efficient way to add integers 
n = 19
sums2 = 0
while (n > 0):
    digit = n % 10
    sums2 += digit * digit
    n = math.floor(n / 10)

print(sums2)

# Return len of smallest word in array
strs = ["flower","flow","flight"]
small = min(len(i) for i in strs)
print(small)

# Return string of shortest length in array
strings = ["some", "example", "words", "that", "am", "fond", "of"]
print(min(strings, key=len))

# Returns all indices in a list for an element
nums = [0,1,0,3,0,12,0]
indices = [i for i, x in enumerate(nums) if x == 0]
print(indices)

#Make a shallow copy of list
# Here we are using the more elegant way, string slicing,
# however you can also just use the library method .copy()
arr9 = [3,2,1]
arr9_shallow = arr9[:]
print(arr9_shallow)
