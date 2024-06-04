# https://builtin.com/data-science/sliding-window-algorithm

# Maximum Sum Subarray of Size K
def getMaxSum(arr, k) -> int:
    max_sum = 0
    window_sum = 0
    start = 0

    for i in range(len(arr)):
        window_sum += arr[i]
        if ((i + 1 - start) == k):
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[start]
            start += 1
    
    return max_sum


# Given an array of positive integers and a positive number k,
# find the maximum sum of any contiguous subarray of size k

# The subarray [1, 7] is the sum of the maximum sum.
# So output 8

arr = [3, 5, 2, 1, 7]
k = 2
print(getMaxSum(arr, k))

#####################################################################################################################

# Count Occurrences of Anagram
def countAnagram(text, word) -> int:
    start = 0
    count = 0
    n = len(word)
    set_word = set(word)
    for i in range(len(text)):
        if((i + 1 - start) == n):
            set_window = set(text[start:i+1])
            if set_window == set_word:
                count += 1
                start += 1
        
    return count

# Given a word and a text, return the count of occurrences of the anagrams of the word in the text.
# Words “got,” “otg” and “ogt” are anagrams of “got.”

text = 'gotxxotgxdogt'
word = 'got'
print(countAnagram(text, word))
