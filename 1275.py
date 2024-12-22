class Solution:
    def check(self, board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] != -1:
                return f"{board[i][0]}"
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != -1:
                return f"{board[0][i]}"
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != -1:
            return f"{board[0][0]}"
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != -1:
            return f"{board[0][2]}"
        
        for row in board:
            if -1 in row:
                return "Pending"
        
        return "Draw"
        


    def tictactoe(self, moves: List[List[int]]) -> str:
        matt = [[-1,-1,-1], [-1,-1,-1], [-1,-1,-1]]

        i = "x"
        for move in moves:
            matt[move[0]][move[1]] = i
            if i == "0":
                i = "x"
            else:
                i = "0"

        
        if self.check(matt) == 'x':
            return "A"
        if self.check(matt) == '0':
            return "B"
        return self.check(matt)
        
