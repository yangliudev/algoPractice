A = 'abcde'
B = 'cdeab'

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        counter = 0

        if len(A) == 0 and len(B) == 0:
            return True
        while counter < len(A):
            temp = A[1:]
            A = temp + A[0]
            if A == B:
                return True
            else:
                counter += 1
        return False
            
            

print(Solution().rotateString(A,B))