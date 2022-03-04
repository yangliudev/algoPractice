nums1 = [3,0,1]
nums2 = [9,6,4,2,3,5,7,0,1]
nums3 = [0,1,2]
nums = [1,2,3]

sort_nums = sorted(nums2)
temp = sort_nums[0]

if 0 not in sort_nums:
    print(0)
else:
    for i in range(1, len(sort_nums)):
        if temp + 1 == sort_nums[i]:
            temp += 1
        if temp == max(sort_nums):
            print(max(sort_nums) + 1)
    print(temp + 1)

#the above solution works but the time complexity is awful so lets try a different approach

nums = [0,1,2]

max_ = nums[0]
for i in range(0, len(nums)):
    if (nums[i] > max_):
        max_ = nums[i]

flags = []

for i in range(0, max_ + 1):
    flags.append(False)


for i in range(0, len(nums)):
    num = nums[i]
    flags[num] = True
    
for i in range(0, len(flags)):
    if flags[i] == False:
        print(i)
print(max_ + 1)