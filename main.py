# Each point in grid is represented by a letter of the color of the piece in it or 0 for empty
# Colors: l (lime), y (yellow), b (blue), r (red), g (green), o (orange), p (purple), c (cyan), d (dark blue), i (pink), 0 (empty)
import msvcrt
import os
import threading
import time
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

level20 = [['l','0','0','0','0','p','p','0','b','b'],
               ['l','0','g','0','0','p','i','0','0','b'],
               ['l','l','g','g','0','p','i','0','0','b'],
               ['0','0','g','g','0','i','i','0','d','b'],
               ['0','0','0','0','0','0','i','d','d','d']]

level2000 =   [['l','o','o','o','o','p','p','c','b','b'],
               ['l','o','g','o','r','p','i','c','c','b'],
               ['l','l','g','g','r','p','i','c','c','b'],
               ['0','0','g','g','r','i','i','c','d','b'],
               ['0','0','0','0','r','r','i','d','d','d']]

level115 =    [['0','0','0','0','0','p','p','p','0','0'],
               ['0','0','0','0','g','g','g','p','0','0'],
               ['0','0','0','0','g','g','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','0','0']]

level50 =     [['l','0','0','0','0','0','o','o','o','o'],
               ['l','0','0','0','0','0','0','o','0','0'],
               ['l','l','d','d','d','b','b','b','b','0'],
               ['0','0','d','0','d','b','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','0','0']]

level72     = [['y','y','i','i','i','i','0','0','0','0'],
               ['y','r','i','i','r','0','0','0','0','0'],
               ['y','r','r','r','r','0','0','0','g','0'],
               ['y','0','0','0','0','0','0','b','g','g'],
               ['0','0','0','0','b','b','b','b','g','g']]

leveltest = [['l','l','l','i','c','c','c','c','0','0'],
          ['l','d','l','i','r','c','c','0','0','0'],
          ['d','d','i','i','r','p','y','y','y','y'],
          ['b','d','b','i','r','p','p','p','o','y'],
          ['b','b','b','b','r','r','o','o','o','o']]
           


all_pieces = {
    'la' : [['l','l','l'],
            ['l','0','l']],
    'lb' : [['l','l','l'],
            ['l','0','0']],
    'ga' : [['g','g','g'],
            ['g','g','0']],
    'gb' : [['g','g','g'],
            ['0','g','0']],
    'pa' : [['p','p','p'],
            ['0','p','p']],
    'pb' : [['p','0','0'],
            ['p','p','p']],
    'da' : [['d','0','d'],
            ['d','d','d']],
    'db' : [['d','d','d'],
            ['0','d','0']],
    'ya' : [['y','y','y','y'],
            ['0','0','y','y']],
    'yb' : [['y','0','0','0'],
            ['y','y','y','y']],
    'oa' : [['o','o','o','o'],
            ['o','0','o','0']],
    'ob' : [['o','o','o','o'],
            ['0','o','0','0']],
    'ra' : [['r','r','r','r'],
            ['r','0','0','0']],
    'rb' : [['r','r','r','r'],
            ['r','0','0','r']],
    'ia' : [['i','i','i','i'],
            ['i','i','0','0']],
    'ib' : [['i','i','i','i'],
            ['0','0','i','0']],
    'ba' : [['b','0','b','0'],
            ['b','b','b','b']],
    'bb' : [['b','b','b','b'],
            ['b','0','0','0']],
    'ca' : [['c','c','c','c'],
            ['0','c','c','0']],
    'cb' : [['c','c','c','c'],
            ['0','c','0','0']],    
}


def print_board(board):
    print('\n')
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



def find_free_spots(board):
    free_spaces = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == '0':
                free_spaces.append((row,col))
    return free_spaces


# Main idea - get a free spot and create 4 3x2 and 4 4x2 patterns -> up right down left.
# All have the same origin point (too left) and are rotated 90 degrees clockwise
# Compare all those small portions with all the piece masks and if one fits use that and call the function again
# to find the next free spot.
# Repeat until there are no more free spots or no free pattern can be created in which case return False
# If the starting point yields no results use next free spot and repeat the process
# Yes it is a long algorithm but it is the only one I could think of rn

# Katra rekursijas soli ejam cauri atlikusajiem gabaliem un meklejam pirmo vietu kur ielikt gabalu
# Ja nav kur ielikt esoso gabalu atgriezamies un meklejam nakamo gabalu

  
def get_pattern(board, row, col, direction, length):
    if direction == 1 and col < len(board[0]) - 1 and row >= length - 1:
        return [[board[row-x][col] for x in range(length)],[ board[row-x][col+1] for x in range(length)]]
    elif direction == 2 and col <= len(board[0]) - length and row < len(board) - 1:
        return [[board[row][col+x] for x in range(length)],[ board[row+1][col+x] for x in range(length)]]
    elif direction == 3 and col > 0 and row <= len(board) - length:
        return [[board[row+x][col] for x in range(length)],[ board[row+x][col-1] for x in range(length)]]
    elif direction == 4 and col >= length and row > 0:
        return [[board[row][col-x] for x in range(length)],[ board[row-1][col-x] for x in range(length)]]
    #print("No pattern found")
    return None



def fits(field,piece):
    if field == None : return False
    
    for row in range(len(field)):
        for col in range(len(field[0])):
            if field[row][col] != '0' and piece[row][col] != '0':
                #print('spot taken')
                return False
    return True

#Rotations from origin pointing: 1-up 2-right 3-down 4-left
def insert(board,row,col,piece,rot):
    #piece lenght
    n = len(piece[0])

    if rot == 1 :
        for i in range(n):
            if board[row-i][col] == '0':
                board[row-i][col] = piece[0][i]
            if board[row-i][col+1] == '0':
                board[row-i][col+1] = piece[1][i]
    elif rot == 2 :
        for i in range(n):
            if board[row][col+i] == '0':
                board[row][col+i] = piece[0][i]
            if board[row+1][col+i] == '0':
                board[row+1][col+i] = piece[1][i]
    elif rot == 3 :
        for i in range(n):
            if board[row+i][col]  == '0':
                board[row+i][col] = piece[0][i]
            if board[row+i][col-1]  == '0':
                board[row+i][col-1] = piece[1][i]
    elif rot == 4 :
        for i in range(n):
            if board[row][col-i]  == '0':
                board[row][col-i] = piece[0][i]
            if board[row-1][col-i]  == '0':
                board[row-1][col-i] = piece[1][i]
            
def insert_reverse(board,row,col,piece,rot):
    n = len(piece[0])
    
    if rot == 1 :
        insert(board,row-n+1,col+1,piece,3)
    elif rot == 2 :
        insert(board,row+1,col+n-1,piece,4)
    elif rot == 3 :
        insert(board,row+n-1,col-1,piece,1)
    elif rot == 4 :
        insert(board,row-1,col-n-1,piece,2)


def get_remaining_pieces(board):
    used_pieces = []
    for row in board:
        for cell in row:
            if cell not in used_pieces and cell != '0':
                used_pieces.append(cell)

    remaining_pieces = [key for key in all_pieces.keys() if key[0] not in used_pieces]

    return remaining_pieces

def remove_piece(board, piece):
    letter = piece[0]
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == letter:
                board[row][col] = '0'


def get_inverse_pattern(pattern):
    if pattern == None: return None
    inverse_pattern = [row[::-1] for row in pattern[::-1]]
    return inverse_pattern





def find_spot_and_place(board, piece):
    piece_length = len(piece[0])
    free_spots = find_free_spots(board)
    #if not free_spots:
    #    return False
    
    #row , col = free_spots[0]
    #print(f'free spot at {row} {col}')
    
    for row , col in free_spots:
        for orientation in range(1,5):
            pattern = get_pattern(board, row ,col , orientation, piece_length)
            if fits(pattern, piece):
                insert(board, row, col, piece, orientation)
                return True
            inverse_pattern = get_inverse_pattern(pattern)
            #print(inverse_pattern)
            if fits(inverse_pattern, piece):
                #print(f'inverse fits at {row} {col} {orientation}')
                insert_reverse(board, row, col, piece, orientation)
                return True
    #print('No spot found')
    return False

moves = 0

def solve(board, remaining_pieces):
    global moves
    moves += 1
    if moves % 100000 == 0:
        print(moves)
    #print('Solving')
    if board[0][6] == 'o':
        msvcrt.getch()
    
    #print(remaining_pieces)
    if not remaining_pieces and find_free_spots(board):
        #print('No more pieces but free spots')
        return False
    if not remaining_pieces:
        #print('No more pieces')
        return True
    
    for piece in remaining_pieces:
        #print(f'Trying piece {piece} out of {remaining_pieces}')
        # Try to find a spot and if we can place a piece
        # Go further
        print_board(board)
        if find_spot_and_place(board, all_pieces[piece]):
            if solve(board, get_remaining_pieces(board)):
                #print('Solved')
                return True
            else:
                remove_piece(board, piece)
                #print('Not solved')
        # Else we try next piece in this branch
            
                 

def testgame(level):
    print_board(level)
    solve(level, get_remaining_pieces(level))
    print_board(level)

# print_board(level1)
# solve(level1, get_remaining_pieces(level1))
# print_board(level1)

# print_board(level20)
# solve(level20, get_remaining_pieces(level20))
# print_board(level20)
# print_board(level115)
# solve(level115, get_remaining_pieces(level115))
# print_board(level115)

testgame(level72)







