# manipulating arrays in place
# https://mecha-mind.medium.com/ds-algo-problems-rotate-or-modify-array-in-place-16eae7bd335d

class Solution(object):
    # rotate no restrictions
    # k is always positive
    def rotate (self, nums, k):
        n = len(nums)
        k = k % n
        start = []
        end = []
        cut = n - k
        for i in range(n):
            if i < cut:
                start.append(nums[i])
            else:
                end.append(nums[i])
      
        res = end + start
        return res

    # rotate in-place
    def rotate_in_place(self, nums, k):
        m = -1
        
        for i in range(len(nums)):
            start = i
            u = nums[start]

            while True:
                j = (start+k) % len(nums)
                m = max(m, j)
                v = nums[j]
                nums[j] = u
                start = j
                u = v
                if start == i:
                    break
            
            if m == len(nums)-1:
                break
        
        return nums

nums = [1,2,3,4,5,6,7]
k = 3
print('No Restrictions: ', Solution().rotate(nums, k))
print('In Place: ', Solution().rotate_in_place(nums, k))
