from typing import List

nums = [2, 2, 3, 1]

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        set_nums = set(nums)
        sort_nums = sorted(set_nums, reverse=True)
        
        if len(sort_nums) == 1:
            return nums[0]
        elif len(sort_nums) == 2:
            return max(sort_nums)
        else:
            return sort_nums[2]



print(Solution().thirdMax(nums))













# nums = [3,3,3,3,4,3,3,3,3]
# nums1 = [2, 1]

# to_set = list(set(nums))
# print(to_set)
# print(nums)

# print(nums[1:])
# print(nums[:-1])

# if nums[1:] == nums[:-1]:
#     print(nums[0])

# if len(nums) == 2 or len(to_set) == 2:
#     print(max(nums))
# elif len(to_set) > 2:
#     print(to_set[-3])