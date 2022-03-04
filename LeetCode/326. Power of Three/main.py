'''
Given an integer, write a function to determine if it is a power of three.
'''

"""
This code works but it is brute force, thus extremely slow. Not ideal!!
n = 59048

if n == 0:
    print(False)

i = 0
while i <= n:
    if pow(3, i) == n:
        print(True)
    i += 1
print(False)
"""

n = 27

while n >= 1:
    if n % 3 == 0:
        n /= 3
    elif n == 1:
        print(True)
        break
    else:
        print(False)
        break