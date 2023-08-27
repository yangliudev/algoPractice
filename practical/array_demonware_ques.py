# Write a function
# that, given an array A of N integers,
# returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

A = [-1, -4, 1, 5, 9, 99]

def solution(A):
    sort_set_arr = list(set(sorted(A)))
    print(sort_set_arr)
    
    #remove negatives
    i = 0
    while i < len(sort_set_arr):
        if sort_set_arr[i] < 0:
            sort_set_arr.pop(i)
        else:
            i += 1

    i = 0
    j = 1
    while j < len(sort_set_arr):
        if sort_set_arr[i] + 1 == sort_set_arr[j]:
            i += 1
            j += 1
        else:
            return sort_set_arr[i] + 1

    return sort_set_arr[-1] + 1

print(solution(A))