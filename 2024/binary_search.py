# Time complexity: O(log n)

def binary_search(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid

nums = [1, 3, 2, 5, 4]
target = 4
print(binary_search(nums, target))
