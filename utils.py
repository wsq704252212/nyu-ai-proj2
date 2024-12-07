"""
Team members:
Zan Ni (zn2161)
Siqi Wan (sw6195)
"""


def read_input(file_path):
    """
    Reads the input file and returns the board, vertiDots, horiDots
    """

    board = []
    vertiDots = []
    horiDots = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Lines 2-31: Workspace grid representation
        for line in lines[0:9]:
            row = list(map(int, line.strip().split()))
            board.append(row)
        for line in lines[10:19]:
            row = list(map(int, line.strip().split()))
            vertiDots.append(row)
        for line in lines[20:28]:
            row = list(map(int, line.strip().split()))
            horiDots.append(row)

    return board, vertiDots, horiDots


# utils.py

def write_output(file_path, solution):
    """
    Writes the output to the specified file in the required format.
    """

    with open(file_path, 'w') as file:
        for row in solution:
            row_str = ' '.join(map(str, row))
            file.write(f"{row_str}\n")



def getRemainValueAndDegree(board, vertiDots, horiDots, coord):
    # check dot constraints
    availableDotValues = getDotaAvailableValue(board, vertiDots, horiDots, coord)
   
    # check if value is used by neighbour
    availableValues = [1] * 10
    degree = 0
    # check neighbour in the same column
    for i in range(9):
        if i == coord[0]:
            continue
        v = board[i][coord[1]]
        availableValues[v] = 0
        if v == 0:
            degree = degree + 1
    # check neighbour in the same row
    for j in range(9):
        if j == coord[1]:
            continue
        v = board[coord[0]][j]
        availableValues[v] = 0
        if v == 0:
            degree = degree + 1
    # check neighbour in the same 3*3 block
    block = (int(coord[0]/3), int(coord[1]/3))
    for i in range(block[0] * 3, block[0] * 3 + 3):
        for j in range(block[1] * 3, block[1] * 3 + 3):
            if i == coord[0] or j == coord[1]:
                continue
            v = board[i][j]
            availableValues[v] = 0
            if v == 0:
                degree = degree + 1
    
    # get remain value
    availableValues = arrayAnd(availableValues, availableDotValues)

    remainValue = []
    for i in range(1, 10):
        if availableValues[i] == 1:
            remainValue.append(i)
    return remainValue, degree

# return the available value under the all dot constraints
# '1' means the value is available for variable
def getDotaAvailableValue(board, vertiDots, horiDots, coord):
    availableValues = [1] * 10
    i, j = coord[0], coord[1]
    # check left dot
    if j > 0:
        constraints = getDotConstraints(vertiDots[i][j-1], board[i][j-1])
        availableValues = arrayAnd(availableValues, constraints)
    # check right dot
    if j < 8:
        constraints = getDotConstraints(vertiDots[i][j], board[i][j+1])
        availableValues = arrayAnd(availableValues, constraints)
    # check up dot
    if i > 0:
        constraints = getDotConstraints(horiDots[i-1][j], board[i-1][j])
        availableValues = arrayAnd(availableValues, constraints)
    # check down dot 
    if i < 8:
        constraints = getDotConstraints(horiDots[i][j], board[i+1][j])
        availableValues = arrayAnd(availableValues, constraints)
    return availableValues

# return constaints, '1' means the value is available for variable
def getDotConstraints(color, neighbour):
    constraints = [0] * 10
    if color == 0:
        return [1] * 10
    if color == 1:
        if neighbour == 0:
            return [1] * 10
        else:
            if neighbour < 9:
                constraints[neighbour+1] = 1
            if neighbour > 1:
                constraints[neighbour-1] = 1
            return constraints
    if color == 2:
        if neighbour == 0:
            return [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]
        else:
            if neighbour * 2 <= 9:
                constraints[neighbour * 2] = 1
            if neighbour % 2 == 0 and neighbour / 2 >= 1:
                constraints[int(neighbour / 2)] = 1
            return constraints
                

def arrayAnd(arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        arr.append(arr1[i] & arr2[i])
    return arr