#Kadane's algorithm is the most optimal way to solve
#for questions that ask to find a maximum subarray in an array
#Runs in linear time with O(N)

#Refer to leetcode question 53. Maximum Subarray https://leetcode.com/problems/maximum-subarray/
# https://www.youtube.com/watch?v=86CQq3pKSUw
# https://leetcode.com/problems/maximum-subarray/discuss/915172/99.42-faster-87-memory-Python
nums = [-2,1,-3,4,-1,2,1,-5,4]

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #Kadane's Algorithm
        
        max_curr = nums[0]
        max_global = nums[0]
        
        for i in range(1, len(nums)):
            max_curr = max(nums[i], nums[i] + max_curr)
            if max_curr > max_global:
                max_global = max_curr
                
        return max_global

print(Solution().maxSubArray(nums))