"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            print("i = %d, nums[i] = %d" % (i, nums[i]))
            for j in range(i + 1, len(nums)):
                print("\tj = %d, nums[j] = %d" % (j, nums[j]))
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
'''
    def betterTwoSum(self, nums, target):
        complement_index_dictionary = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            complement_index_dictionary["i"]
'''

nums = [90, 12, 2, 9, 11, 15, 7]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result)