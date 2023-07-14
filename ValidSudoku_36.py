'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
'''



def isValidSudoku(board):
    boardSize=len(board)
    rows=[{} for i in range(boardSize)]
    columns=[{} for i in range(boardSize)]
    squares=[{} for i in range(boardSize)]
    squareNum={(0,0):0,(0,1):1,(0,2):2,(1,0):3,(1,1):4,(1,2):5,(2,0):6,(2,1):7,(2,2):8}
      
    for rowNum in range(boardSize):
        for columnNum in range(boardSize):
            if board[rowNum][columnNum]!='.':
                curPos=board[rowNum][columnNum]
                if curPos in rows[rowNum]:
                    return False
                rows[rowNum][curPos]=columnNum
                if curPos in columns[columnNum]:
                    return False
                columns[columnNum][curPos]=rowNum
                if curPos in squares[squareNum[((columnNum-columnNum%3)/3,(rowNum-rowNum%3)/3)]]:
                    return False          
                squares[squareNum[((columnNum-columnNum%3)/3,(rowNum-rowNum%3)/3)]][curPos]=(rowNum,columnNum)
    return True

test=isValidSudoku(
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]) 

print(test)

'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        boardSize=len(board)
        rows=[{} for i in range(boardSize)]
        columns=[{} for i in range(boardSize)]
        squares=[{} for i in range(boardSize)]
        squareNum={(0,0):0,(0,1):1,(0,2):2,(1,0):3,(1,1):4,(1,2):5,(2,0):6,(2,1):7,(2,2):8}
      
        for rowNum in range(boardSize):
            for columnNum in range(boardSize):
                if board[rowNum][columnNum]!='.':
                    curPos=board[rowNum][columnNum]
                    if curPos in rows[rowNum]:
                        return False
                    rows[rowNum][curPos]=columnNum
                    if curPos in columns[columnNum]:
                        return False
                    columns[columnNum][curPos]=rowNum
                    if curPos in squares[squareNum[((columnNum-columnNum%3)/3,(rowNum-rowNum%3)/3)]]:
                        return False          
                    squares[squareNum[((columnNum-columnNum%3)/3,(rowNum-rowNum%3)/3)]][curPos]=(rowNum,columnNum)
        return True
'''