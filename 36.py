from itertools import chain

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flat_list = list(chain.from_iterable(board))
        board_li = board
        board_column = []

        #checking rows:
        for x in board:
            for i in range(len(x)):
                #print(x[:i], x[i], x[i+1:])
                if x[i] != ".":
                    if x[i] in x[:i] or x[i] in x[i+1:]:
                        return False

        board_column = []
        for i in range(0, 9):
            temp_li = []
            j = i
            while True:
                temp_li.append(flat_list[j])
                j = j + 9
                if j >= 81:
                    break
            board_column.append(temp_li)

        #print(board_column)
        for x in board_column:
            for i in range(len(x)):
                #print(x[:i], x[i], x[i+1:])
                if x[i] != ".":
                    if x[i] in x[:i] or x[i] in x[i+1:]:
                        return False
        
        square_li = []
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                square = []
                for r in range(3):
                    for c in range(3):
                        square.append(board[row+r][col+c])
                square_li.append(square)
        
        for x in square_li:
            for i in range(len(x)):
                #print(x[:i], x[i], x[i+1:])
                if x[i] != ".":
                    if x[i] in x[:i] or x[i] in x[i+1:]:
                        return False
                
        return True
