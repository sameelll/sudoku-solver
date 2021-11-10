#*** PROJECT: SUDOKU SOLVER ***#


# Printing the board:

def print_board(board):  

    if board is None:
        print("No Solution")
        return
    
    line = "-"*25
    print(line)
    for i in range(len(board)):
       
        line_to_print = "| "

        if i != 0 and i % 3 == 0:

            print(line)

        for j in range(len(board)): 

            if board[i][j]==0:

                board[i][j]= " "   

            if j != 0 and j % 3 == 0:

                line_to_print += "| " + str(board[i][j]) + " "
                    
            else:
                
                line_to_print += str(board[i][j]) + " "
                
        print(line_to_print + "|")

    print(line)      
#**************************************************

# Finding where zero is:

def find_zero(board):

    for i in board:

        where_zero = []

        for k in range(len(board)): 

            for j in range(len(i)):
        
                if board[k][j]==0 or board[k][j]== " " :

                    where_zero.append(k)
                    where_zero.append(j)
                    return where_zero

        else:
            where_zero=[]
            return where_zero
        
#**************************************************

# Is the value valid? :

def is_valid(board, row, col, value):

    grid_row = row // 3
    grid_col = col // 3
   
    for i in range(len(board)):

        if board[row][i]!=value and board[i][col]!=value:
            continue           
        validity=False
        return validity  

    for i in range(3):
        for j in range(3):
            if board[3*grid_row + i][3*grid_col + j] == value:
                validity=False
                return validity
        
    else:
        validity=True
        return validity    

#**************************************************  

#Solution part:

def solve(board):

    zero_finder=find_zero(board)
    
    if zero_finder==[]:

        return board

    else:
            
        for i in range(1,10):

            row = zero_finder[0]
            col = zero_finder[1]
            validation=is_valid(board, row, col, i)
            
            if validation==True:
                
                board[row][col]=i
                sol=solve(board)
                
                if sol is not None:
                    return sol

                board[row][col]=0

    return  None    

#**************************************************

#Defining the board:

board= [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

#**************************************************

#Putting the titles:

#Sudoku: 

print("                  ")
print("         SUDOKU:")    
print_board(board) 

#Solution:

print("                  ")
print("                  ")
print("        SOLUTION: ")
solve(board)
print_board(board)

#**************************************************