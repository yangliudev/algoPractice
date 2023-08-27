# Creating an empty matrix
cols = 4
rows = 5
array = [[0 for i in range(cols)] for j in range(rows)]
#>>> array
#[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
#print(array)


#another way
matrix = [[0]*5 for i in range(5)]

# List comprehension way to transpose matrix (Transpose means rows become cols and vice versa)
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
print([[matrix1[col][row] for col in range(len(matrix1))] for row in range(len(matrix1[0]))])

# Another way to transpose that is easier to understand
class Solution:
    def transpose(self, A):
        R = len(A)
        C = len(A[0])
        transpose = []
        for c in range(C):
            newRow = []
            for r in range(R):
                newRow.append(A[r][c])
            transpose.append(newRow)
        return transpose