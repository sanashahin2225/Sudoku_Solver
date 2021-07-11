#This function is used to check WHETHER THE NUMBER TO BE PLACED IS VALID OR NOT
def is_valid(board,row,col,val):
    if val in board[row]:
        return False
    else:
        for j in range(9):
            if board[j][col] == val:
                return False
    new_row = row % 3
    new_col = col % 3
    for i in range(new_row):
        for j in range(new_col):
            if val == board[new_row][new_col]:
                return False
    return True

#This function is used to FIND THE EMPTY CELL AND IT WILL RETURN THE (ROW,COL) 
def find_empty(board):
    for i in range(9):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i,j)

#This function is used for PRINTING THE BOARD
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------------------------")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print(" | ",end='')
            print(board[i][j],end=' ')
        print("\n")


#Main Function (Recursive)

def solve(board):
    if not find_empty(board):
        return board
    for i in range(1,10):
        row,col = find_empty(board)
        if is_valid(board,row,col,i):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False  


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

solve(board)
print_board(board)
