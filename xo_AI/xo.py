def row_win(i, board) -> int:
    if board[i][0] != 0 and (board[i][0] == board[i][1] and board[i][0] == board[i][2]):
        return board[i][0]
    return 0

def col_win(i, board) -> int:
    if board[0][i] != 0 and (board[0][i] == board[1][i] and board[0][i] == board[2][i]):
        return board[0][i]
    return 0

def diag_win(i, board) -> int:
    if board[0][0] != 0 and (board[0][0] == board[1][1] and board[0][0] == board[2][2]):
        return board[0][0]
    if board[0][2] != 0 and (board[0][2] == board[1][1] and board[0][2] == board[2][0]):
        return board[0][2]
    return 0

class XO:

    def __init__(self) -> None:
        self.board = [[0] * 3 for i in range(3)]
    
    def win(self):
        for i in range(3):
            winner = row_win(i, self.board)
            if winner != 0:
                return winner
            
            winner = col_win(i, self.board)
            if winner != 0:
                return winner

        winner = diag_win(i, self.board)
        if winner != 0:
            return winner
        
        return 0
    
    def play(self, player, pos):
        if (self.board[pos[0]][pos[1]] != 0):
            return 1
        else:
            self.board[pos[0]][pos[1]] = player
            return 0
    
    def print(self):
        for i in range(3):
            for j in range(3):
                if (self.board[i][j] == 0):
                    print('#', end = '')
                if (self.board[i][j] == 1):
                    print('X', end = '')
                if (self.board[i][j] == 2):
                    print('O', end = '')
            print('')
    
    def reset(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = 0


def run_real():
    running = 1
    xo = XO()
    counter = 0
    while running and counter < 9:
        player = counter % 2 + 1
        counter += 1
        print(f"Player {player} turn to play")
        while xo.play(player, (int(input("Ligne : ")), int(input("Colonne : ")))):
            print("Position already taken")
        xo.print()
        if xo.win() != 0:
            running = 0
            print(f"Player {player} won !")