# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).

#input N      0 1 2 3 4 5 6
#output       0 1 1 2 3 5 8

#Most obvious approach is using recursion

N = 6

class Solution:

    my_dict = {}

    def fib(self, N: int) -> int:
        if N in self.my_dict:
            return self.my_dict[N]
        
        if N == 0:
            self.my_dict[N] = 0
        elif N == 1:
            self.my_dict[N] = 1
        else:
            val = self.fib(N - 1) + self.fib(N - 2)
            self.my_dict[N] = val
        
        return self.my_dict[N]

print(Solution().fib(N))

#Best approach to question in O(N) time

# N = 6

# class Solution:
#     def fib(self, N: int) -> int:
#         if N <= 1:
#             return N

#         arr = [None] * (N + 1)
#         arr[0] = 0
#         arr[1] = 1

#         for i in range(2, N + 1):
#             arr[i] = arr[i-1] + arr[i-2]

#         return arr[-1]


# print(Solution().fib(N))