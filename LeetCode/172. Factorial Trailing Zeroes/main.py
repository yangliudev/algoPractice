'''
Given an integer n, return the number of trailing zeroes in n!

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.


Input: 30   Output: 7
Input: 40   Output: 9

'''

n = 30
fact = 1
counter = 0

# while n > 1:
#     if fact * n % 10 == 0:
#         counter += 1
#         fact /= 10
#     fact *= n
#     n -= 1

# print(fact)
# print(counter)

fact = 1
counter = 0

while n > 1:
    fact = fact * n
    n = n - 1
    
while fact % 10 == 0:
    print(fact)
    fact = int(fact / 10)
    print(fact)
    counter += 1

print(counter)

'''
n     fact      fact_after_operation    counter

10    1         10                      1
9     10        90                      2
8     90        720                     3


n     fact      fact_after_operation    counter

10    1         10  / 10 =  1           1
9     1         9                       1
8     9         72                      3
'''