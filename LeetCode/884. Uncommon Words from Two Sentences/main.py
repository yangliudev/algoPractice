from typing import List

A = "this apple is sweet"
B = "this apple is sour"

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:

        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1

        return [word for word in count if count[word] == 1]

        # temp = []
        # temp2 = []
        # temp3 = []

        # startIndex = 0
        
        # for i in range(len(A)):
        #     endIndex = i
        #     if A[i] == ' ':
        #         temp.append(A[startIndex:endIndex])
        #         startIndex = endIndex + 1
        # temp.append(A[startIndex:])
        


        # startIndex2 = 0

        # for i in range(len(B)):
        #     endIndex = i
        #     if B[i] == ' ':
        #         temp2.append(B[startIndex2:endIndex])
        #         startIndex2 = endIndex + 1
        # temp2.append(B[startIndex2:])

        # temp.extend(temp2)

        # for i in range(len(temp)-1):
        #     if temp[i] == temp[i+1]:
        #         temp3.append(temp[i])
        # return temp3


print(Solution().uncommonFromSentences(A,B))