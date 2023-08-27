import random

number_list = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]
# 11 elements in list

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

def binary_search_recursive(ls, target):
    mid = (len(ls) - 1) // 2

    if len(ls) == 1:
        print('TARGET DOES NOT EXIST')
        return False

    if ls[mid] == target:
        print('FOUND TARGET')
        return True

    if ls[mid] > target:
        binary_search_recursive(ls[:mid+1], target)
    else:
        binary_search_recursive(ls[mid+1:], target)
        
#linear_search(number_list, 5)
#binary_search(number_list, 1)
binary_search_recursive(number_list, 18)
