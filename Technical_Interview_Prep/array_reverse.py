#Reverse an array
arr = [1, 2, 3, 4, 5]

#Easiest method is to use the built in library reverse
arr.reverse()
print(arr)
#########################################################

#Now let's try reversing it without built in help
arr2 = [1, 2, 3, 4, 5]

#Easiest method here is using Python's slicing operator
print(arr2[::-1])
#########################################################

#Finally let's reverse it IN PLACE, this will be the most tricky
arr3 = [1, 2, 3, 4, 5]

left = 0
right = len(arr3) - 1
temp = 0

while left < right:
    temp = arr3[left]
    arr3[left] = arr3[right]
    arr3[right] = temp
    left += 1
    right -= 1

print(arr3)
