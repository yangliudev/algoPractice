"""
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
"""

from typing import List

s = "PPALLL"

class Solution:
    def checkRecord(self, s: str) -> bool:
        for i in range(len(s)-2):
            if s[i] == 'L' and s[i+1] == 'L' and s[i+2] == 'L':
                return False
        if s.count('A') > 1:
            return False
        return True

print(Solution().checkRecord(s))