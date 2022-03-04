'''
The first easy way is below, however this is not in-place
First convert the list to a set to remove all duplicates, then convert it back to a list

return len(list(set(nums)))

'''

nums = [0,0,1,1,1,2,2,3,3,4]

i = 0
while i < len(nums) - 1:
    if nums[i] == nums[i+1]:
        del nums[i]
    else:
        i += 1

print(nums)