# Given a sorted array nums, remove the duplicates
# in-place such that each element appears only once and
# returns the new length.

#Simple solution if you did not have to do it IN PLACE

# nums = [0,0,1,1,1,2,2,3,3,4]

# from typing import List

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         return len(set(nums))

# print(Solution().removeDuplicates(nums))

#Solution 2 to modify IN PLACE

nums = [0,0,1,1,1,2,2,3,3,4]

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                i += 1
                j += 1

        return len(nums)


print(Solution().removeDuplicates(nums))