'''

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

0 1 1 2 3 5 8 13 21 34

'''


'''
Below is a brute force way to calc the fibonacci sequence using recursion.
This is not ideal as the time complexity is gonna be tremendous.

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n-1) + fib(n-2)

print(fib(9))
'''

'''
The code is modified from the first one, implementing memoization (cache values) using a dictionary.
This helps us reduce time complexity by caching/storing values that are already calculated,
instead of calculating the same thing again and again like the method we did above.

my_dict = {}

def fib(n):

    if n in my_dict:
        return my_dict[n]

    if n == 0:
        val = 0
    elif n == 1:
        val = 1
    elif n == 2:
        val = 1
    elif n > 2:
        val = fib(n-1) + fib(n-2)

    my_dict[n] = val
    return val

print(fib(500))
'''