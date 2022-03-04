nums = [4,3,2,7,8,2,3,1]

sort = sorted(nums)
arr = []

for i in range(len(sort)):
    if sort[i] != sort[i+1]:
        arr.append(sort[i+1])

print(arr)