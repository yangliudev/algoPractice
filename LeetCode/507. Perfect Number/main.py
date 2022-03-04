num = 28

arr = []

if num % 2 == 0:
        arr.append(1)
        arr.append(2)

while num > 1:
    if num % 2 == 0:
        num /= 2
        arr.append(num)
    elif num % 2 != 0:
        break

for i in range(len(arr)):
    x = num / arr[i]
    if num % arr[i] == 0 and x not in arr:
        arr.append(x)

print(arr)