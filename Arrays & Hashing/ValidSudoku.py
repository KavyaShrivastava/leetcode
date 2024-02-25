from typing import List

class ValidSudoku:
    def validSudoku(self, board:List[List[str]])->bool:
        n = 9
        rows = [[]for _ in range(n)]
        cols = [[]for _ in range(n)]
        boxes = [[] for _ in range(n)]
        
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
        