# Problem from https://algodaily.com/challenges/find-shortest-palindrome-possible/python

# Return the shortest palindrome of a input string s

from tkinter import E


def shortest_palindrome(s):
    if s == s[::-1]:
        print('True')

    ls = list(s)
    print(ls)

    diff = []

    for i in range(len(ls)//2):
        if ls[i] != ls[-1+i]:
            diff.append()

shortest_palindrome('bubble')
#shortest_palindrome('racecar')

E L B b u b b l e

b u b b l e

b u
e l 

abba 
ababa