'''

We have 2 interesting cases.

1. [-4,-3,-2,-1,60]
if there is only one positive integer in the list,
multiply the positive integer with the 2 lowest negative integers

2. [-4,-3,-2,-1,60,58]
if there is 2 positive integers in the list,
then the same thing applies and you multiply the largest positive integer
with the two smallest negative integers

'''
from typing import List

#nums1 = [1,2,3,4]
nums = [-4,-3,-2,-1,60]

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        sort_nums = sorted(nums)
        
        return max(sort_nums[0] * sort_nums[1] * sort_nums[len(sort_nums) - 1], sort_nums[len(sort_nums) - 3] * sort_nums[len(sort_nums) - 2] * sort_nums[len(sort_nums) - 1])

print(Solution().maximumProduct(nums))
































# pos = []
# neg = []

# for i in range(len(nums)):
#     if nums[i] < 0:
#         neg.append(nums[i])
#     if nums[i] > 0:
#         pos.append(nums[i])

# if len(pos) == 1 or len(pos) == 2:
#     neg1 = min(neg)
#     neg.remove(neg1)

#     neg2 = min(neg)
#     neg.remove(neg2)

#     neg3 = min(neg)

#     print(pos[0] * neg1 * neg2)
# elif len(pos) > 2:
#     pos1 = max(pos)
#     pos.remove(pos1)

#     pos2 = max(pos)
#     pos.remove(pos2)

#     pos3 = max(pos)
#     print(pos1 * pos2 * pos3)
# elif len(pos) == 0:
#     print(neg1 * neg2 * neg3)