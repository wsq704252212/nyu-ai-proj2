from utils import getRemainValueAndDegree

"""
Team members:
Zan Ni (zn2161)
Siqi Wan (sw6195)
"""

# back trace
def backtrace(board, vertiDots, horiDots):
    if isComplete(board):
        return True, board
    var, remainValue = selectUnassignedVar(board, vertiDots, horiDots)
    for v in remainValue:
        i, j = var[0], var[1]
        board[i][j] = v
        result, board = backtrace(board, vertiDots, horiDots)
        if result == True:
            return result, board
        board[i][j] = 0
    return False, board


# check if board is complete
def isComplete(board):
    for row in board:
        for grid in row:
            if grid == 0:
                return False
    return True

# find Unassigned variable with minimum remaining value and degree heuristics
# return variable and remainingValues
def selectUnassignedVar(board, vertiDots, horiDots):
    var = ()
    remainV = 10 * [0]
    maxDegree = -1

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                continue
            remainValue, degree = getRemainValueAndDegree(board, vertiDots, horiDots, (i, j))
            if len(remainValue) < len(remainV):
                var = (i, j)
                maxDegree = degree
                remainV = remainValue
            elif len(remainValue) == len(remainV):
                if degree > maxDegree:
                    var = (i, j)
                    maxDegree = degree
                    remainV = remainValue
    return var, remainV
            
    
