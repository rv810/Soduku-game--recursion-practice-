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

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("------------------") #separate between every 3 rows

        for j in range(len(bo[0])):
            if j%3 == 0 and j != 0: #after every three items print a line
                print(" | ", end="") #"end" stops from going to next line
                
            if j == 8: #print the last item in the list and go to next line
                print(bo[i][j])      
            else: #print current item in list with a space and stay on same line
                print(str(bo[i][j]) + " ", end="")

        
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j) #row, column
    return None

def check(bo, num, position):
    #check row
    for i in range(len(bo[0])):
        if bo[position[0]][i] == num and position[1] != i:
              return False
            
    #check column
    for i in range(len(bo)):
        if bo[i][position[1]] == num and position[0] != i:
            return False

    #check box
    x_section = position[1] // 3
    y_section = position[0] // 3

    for i in range(y_section*3, y_section*3 + 3):
        for j in range(x_section*3, x_section*3 + 3):
            if bo[i][j] == num and (i,j) != position:
                return False

    return True


def solve(bo):
    empty = find_empty(bo)
    if not empty:
        return True
        #base case for recursion (want to get to a point where board is fully solved and no empty slots)
    else:
        row, column = empty
    
    for i in range(1,10):
        if check(bo, i, (row, column)):
            bo[row][column] = i

            if solve(bo):
                return True
        
            bo[row][column] = 0
            
    return False

def main():
    print_board(board)
    solve(board)
    print("\nSolved: \n")
    print_board(board)

        
        
    
        
                        
