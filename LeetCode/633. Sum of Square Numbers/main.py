"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that
a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:

Input: 3
Output: False
"""

c = 5

class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        arr = []

        startIndex = 0
        endIndex = c

        while c >= 0:
            arr.append(c)
            c -= 1

        while startIndex < endIndex:
            midIndex = (startIndex + endIndex) // 2
            x = arr[startIndex] * arr[startIndex] + arr[endIndex] * arr[endIndex]
            if x == arr[0]:
                return True
            elif x > arr[0]:
                startIndex = midIndex
            elif x < arr[0]:
                endIndex = midIndex
        return False

        # oddIterator = 1
        # bValue = 0
        # a = 0
        # b = c - a*a

        # while bValue < b:
        #     bValue +=

        #b = sqrt(c - a^2)
        # a = 0

        # while a*a <= c:
        #     a += 1

        # return a


        # 0 * 0 <= 5
        # 1 * 1 = 1 <= 5
        # 2 * 2 = 4 <= 5
        # 3 * 3 = 9 <= 5

        # n^2 is equal to the sum of the first n odd int
        # 9
        # 1 3 5

print(Solution().judgeSquareSum(c))