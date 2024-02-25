from typing import List

class ValidSudoku:
    def validSudoku(self, board:List[List[str]])->bool:
        n = 9
        rows = [[]for _ in range(n)] #intialise a list of rows 
        cols = [[]for _ in range(n)] # initialise a list of cols 
        boxes = [[] for _ in range(n)] # initialise a list of boxes 
        
        #for every row in board 
        # for every column in board 
        #if this element is present as ., then continue
        #otherwise check for it in the list of rows at the row that this row is indexed 
        #check for it in the column with the same index column
        #and check for it in the boxes where the index is row/3 * 3 + j/3 or j/3*3 + row/3
        #depending ong oing left to right or top to bottom
        #else add these values so the next time they're present, it returns false
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in boxes[(row//3 *3)+ col//3]:
                    return False
                else:
                    rows[row].append(board[row][col])
                    cols[col].append[board[row][col]]
                    boxes[(row//3)*3 + col//3].append(board[row][col])
        return True
        