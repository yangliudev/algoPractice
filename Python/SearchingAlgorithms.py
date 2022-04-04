import random

number_list = [1, 2, 3, 4, 5, 6]

def linear_search(ls, target):
    for num in ls:
        if num == target:
            print('Found number!')
            return

    print('Not found!')

def binary_search(ls, target):
    start = 0
    end = len(ls) - 1
    isFound = False
    while start <= end:
        mid = (start + end) // 2
        if ls[mid] == target:
            print('Number found at index: ', mid)
            isFound = True
        
        if ls[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    if isFound == False:
        print('Number not found!')
        
#linear_search(number_list, 5)
binary_search(number_list, 1)
