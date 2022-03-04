from typing import List

A = [1,2,0,0]
K = 34

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        str_list = [str(i) for i in A]
        strs = ''.join(str_list)
        new_value = K + int(strs)
        return list(str(new_value))


print(Solution().addToArrayForm(A,K))