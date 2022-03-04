from typing import List

nums = [5, 4, 3, 2, 1]

class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:

        nums.sort()
        strs = [str(num) for num in nums]
        print(strs)

        for i in range(len(strs)-2):
            strs[i] = "Gold Medal"
            strs[i+1] = "Silver Medal"
            strs[i+2] = "Bronze Medal"
            break
        
        return strs

print(Solution().findRelativeRanks(nums))