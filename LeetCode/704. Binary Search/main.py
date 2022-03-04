nums = [-1,0,5]
target = 5

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if target not in nums:
            return -1

        if len(nums) == 2:
            if nums[0] == target:
                return 0
            else:
                return 1
        
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        
        while nums[mid] != target:
            if nums[mid] > target:
                right = mid
                mid = (left + right) // 2
            elif nums[mid] < target:
                left = mid
                mid = (left + right) // 2
                if left == mid:
                    mid += 1
                
        return mid

print(Solution().search(nums, target))

'''

nums = [-1,0,3,5,9,12]
target = 9

left = 0
right = 5
mid = 0 + 5 // 2
mid = 2

2 != 9

left = 2
mid = (2 + 5) // 2
mid = 3

left = 3
mid = (3 + 5) // 2
mid = 4

left = 4
mid = (4 + 5) // 2
mid = 4

'''