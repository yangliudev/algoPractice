from typing import List

arr = [1,0,2,3,0,4,5,0]

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        #new_arr = []
        indexes = []

        for i in range(len(arr)):
            if arr[i] == 0:
                indexes.append(i)

        for i in range(len(arr)-1):
            for j in range(len(indexes)):
                if i == indexes[j]:
                    arr[i+1] = 0 

        return arr
        #if len(new_arr) < arr:
            
        

print(Solution().duplicateZeros(arr))