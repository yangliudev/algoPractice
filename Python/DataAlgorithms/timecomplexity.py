# https://www.guru99.com/timeit-python-examples.html
from timeit import timeit

arr = [1,2,3,4,5]
squared = map(lambda x: x * x, arr)
print(list(squared))

print(arr)

print(timeit())

for i in range(len(arr)):
    arr[i] =  arr[i] * arr[i]

print(arr)
print(timeit())