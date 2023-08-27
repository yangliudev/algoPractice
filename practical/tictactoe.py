from typing import List

class TicTacToe:

    # n is the size of the n x n game board
    def __init__(self, n: int):
        self._matrix = [[None]*n for i in range(n)]
        #print(self._matrix)

    def play(self, row: int, col: int , turn: bool):

        # turn == true means x turn
        
        if turn == True:
            self._matrix[row][col] = 'X'
        else:
            self._matrix[row][col] = 'O'

        print(self._matrix)

    def checkRow(self):
        for row in range(len(self._matrix)):
            if len(set(self._matrix[row])) == 1 and self._matrix[row][0] == 'X':
                return 'X wins!'
            elif len(set(self._matrix[row])) == 1 and self._matrix[row][0] == 'O':
                return 'O wins!'

    def checkCol(self):
        return

    def checkDiag(self):
        return

t = TicTacToe(3)
t.play(0,0,True)
t.play(2,0,False)
print(t)



'''

[X, X, X]
[-, -, -]
[O, O, -]

'''