
# Each point in grid is represented by a letter of the color of the piece in it or 0 for empty
# Colors: l (lime), y (yellow), b (blue), r (red), g (green), o (orange), p (purple), c (cyan), d (dark blue), i (pink), 0 (empty)

start_board = [['0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','0','0']]

# There are pieces of 3x2 and 4x2
# Each piece has an A and B version

level1 = [['l','l','l','0','c','c','c','c','g','g'],
          ['l','d','l','0','0','c','c','g','g','g'],
          ['d','d','0','0','0','p','y','y','y','y'],
          ['b','d','b','0','0','p','p','p','0','y'],
          ['b','b','b','b','0','0','0','0','0','0']]


small_pieces = {
    'la' : [[1,1,1],
            [1,0,1]],
    'lb' : [[0,0,1],
            [1,1,1]],
    'ga' : [[0,1,1],
            [1,1,1]],
    'gb' : [[1,1,1],
            [0,1,0]],
    'pa' : [[1,1,1],
            [0,1,1]],
    'pb' : [[1,0,0],
            [1,1,1]],
    'da' : [[1,0,1],
            [1,1,1]],
    'db' : [[1,1,1],
            [0,1,0]],    
}


large_pieces = {
    'ya' : [[1,1,1,1],
            [0,0,1,1]],
    'yb' : [[1,0,0,0],
            [1,1,1,1]],
    'oa' : [[0,1,0,1],
            [1,1,1,1]],
    'ob' : [[1,1,1,1],
            [0,1,0,0]],
    'ra' : [[0,0,0,1],
            [1,1,1,1]],
    'rb' : [[1,1,1,1],
            [1,0,0,1]],
    'ia' : [[1,1,1,1],
            [1,1,0,0]],
    'ib' : [[0,0,1,0],
            [1,1,1,1]],
    'ba' : [[1,0,1,0],
            [1,1,1,1]],
    'bb' : [[1,1,1,1],
            [1,0,0,0]],
    'ca' : [[0,1,1,0],
            [1,1,1,1]],
    'cb' : [[1,1,1,1],
            [0,1,0,0]],
}

def print_board(board):
    for row in board:
        for cell in row:
            print(get_symbols(cell), end=" ")
        print()

def get_symbols(piece):
    colors = {
        'l': "\033[42m" + "L" + "\033[0m",  # Green Background
        'y': "\033[43m" + "Y" + "\033[0m",  # Yellow Background
        'b': "\033[44m" + "B" + "\033[0m",  # Blue Background
        'r': "\033[41m" + "R" + "\033[0m",  # Red Background
        'g': "\033[46m" + "G" + "\033[0m",  # Cyan Background
        'o': "\033[45m" + "O" + "\033[0m",  # Magenta Background
        'p': "\033[47m" + "P" + "\033[0m",  # White Background
        'c': "\033[104m" + "C" + "\033[0m", # Bright Blue Background
        'd': "\033[100m" + "D" + "\033[0m", # Dark Grey Background
        'i': "\033[105m" + "I" + "\033[0m", # Light Magenta Background
        '0': "X"                             # Default/No Color
    }

    return colors.get(piece.lower(), "X")  # Return the color or "X" if not found



def find_free_spot(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '0':
                return row, col
    return None


# Main idea - get a free spot and create 4 3x2 and 4 4x2 patterns -> up right down left.
# All have the same origin point (too left) and are rotated 90 degrees clockwise
# Compare all those small portions with all the piece masks and if one fits use that and call the function again
# to find the next free spot.
# Repeat until there are no more free spots or no free pattern can be created in which case return False
# If the starting point yields no results use next free spot and repeat the process
# Yes it is a long algorithm but it is the only one I could think of rn
  
def get_pattern1(board,row,col):
    if col < 9 and row > 1:
        return [[board[row-x][col] for x in range(3)],
                [board[row-x][col+1] for x in range(3)]]

def get_pattern2(board,row,col):
    if col < 8 and row < 5:
        return [[board[row][col+x] for x in range(3)],
                [board[row+1][col+x] for x in range(3)]]

def get_pattern3(board,row,col):
    if col > 0 and row < 3:
        return [[board[row+x][col] for x in range(3)],
                [board[row+x][col-1] for x in range(3)]]

def get_pattern4(board,row,col):
    if col > 1 and row > 0:
        return [[board[row][col-x] for x in range(3)],
                [board[row-1][col-x] for x in range(3)]]

def fits(field,piece):
    if not field or not piece : return False
    if len(field[0]) !=  len(piece[0]) : return False
    for row in range(len(field)):
        for col in range(len(field[0])):
            if field[row][col] != '0' and piece[row][col] == 1:
                return False
    return True

print(fits(get_pattern1(level1,1,2),small_pieces['pb']))

print_board(level1)
print(get_pattern4(level1,2,2))
