import math
reviews = [
    [1, 2],
    [2, 5],
    [2, 5],
    [0, 1]
]
threshold = 0
class Solution:
    def solve(self, reviews, threshold):
        
        threshold /= 100

        rows = len(reviews)
        cols = len(reviews[0])

        left = 0
        right = 0

        for row in range(rows):
            for col in range(cols-1):
                left += reviews[row][col]
                right += reviews[row][col+1]

        print(left)
        print(right)

        if left / right == threshold:
            return 0
        
        print(threshold)
        round_ans = round((threshold * right - left) / (1 - threshold),5)
        print(round_ans)
        if round_ans < 0:
            return 0
        else:
            return math.ceil(round_ans)

print(Solution().solve(reviews,threshold))