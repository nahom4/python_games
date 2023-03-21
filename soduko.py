board = [['-1' for x in range(9)] for _  in range(9)]
def column_value(col):
    return[x[col] for x in board]
def solve(board):

    cell = next()

    if cell==(None,None):
        return True
    for x in range(10):
        if  valid(cell,x):
            row,col=cell
            board[row][col] = x
            

            if solve(board):

                print(board)
                return True

    return False


def next():
    for x in range(9):
        for y in range(9):


            if board[x][y]== '-1':
            
                return (x,y)
            else:
                continue
    return(None,None)
def valid(cell,x):
    #let's do row check
    row,col= cell
    if x in board[row]:
        return False
    #let's do column check
    if x in column_value(col):
        return False
    #let's check the little squares
    start_row = (row%3)*3
    start_col = (col%3)*3
    for val in range(start_row,start_row+3):
        for value in range(start_col, start_col + 3):
            if board[val][value] == x:
                return False

    return True


if __name__ == '__main__':

    if (solve(board)):
        print('the puzzele was solved ')
    else:
        print('unable to solve the puzzle')

