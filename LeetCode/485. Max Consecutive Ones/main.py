from typing import List

nums = [1,1,0,1,1,1]

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x = 0
        y = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                x += 1
            
            if nums[i] == 0:
                if x > y:
                    y = x
                x = 0
                
        if x > y:
            return x
        else:
            return y

print(Solution().findMaxConsecutiveOnes(nums))






# nums = [1,1,0,1,1,1]
# nums1 = [1,0,1,1,0,1]

# n = 0
# m = ''
        
# for i in range(len(nums)):

#     if nums[i] == 1:
#         n += 1

#     if nums[i] == 0:
#         m = n
#         n = 0

# if m > n:
#     print(m)
# else:
#     print(n)

# print(n)
# print(m)

'''
loop through the list, if there are consecutive 1's add 1 to our empty variable n.
set n to another variable m to hold this value so that we are able to compare the values after.
if we encounter a 0 stop adding 1 to n.
compare both variables n and m.
if one of the variables is larger than set that to n.
'''