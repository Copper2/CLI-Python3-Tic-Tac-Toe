'''
While True:
- Display a CLI 3x3 board
- Pick x or o randomly to start
- Options for p1 or p2:
- Check draw (whether the board is fully filled)
- Check win (whether one of the player has won):
    + Check the rows
    + Check the cols:
    + Check the 2 diagonals
'''
import random as r


class TicTacToe:
    def __init__(self):
        self.board = \
            [['x', '-', '-'], 
             ['x', '-', '-'], 
             ['x', '-', '-']]

        self.p1_sign = None
        self.p2_sign = None

    # Draw a 3x3 board in terminal
    # This function keeps track of the game or also print it out
    def draw_board(self):
        for row in range(3):
            for col in range(3):
                if col == 2:
                    print(self.board[row][col])
                else:
                    print(self.board[row][col], end="")
                
    # Choose a rorom player (x or o) to start
    def choose_player(self):
        player_start_first = r.randint(1,2)
        if player_start_first == 1:
            self.p1_sign = 'x'
            self.p2_sign = 'o'
            print('x starts first')
        elif player_start_first == 2:  
            self.p1_sign = 'o'
            self.p2_sign = 'x'
            print('o starts first')


    # Implements the options of p1 or p2
    def go(self, player):
        player_row = int(input(f"Player {player} chooses row: "))
        player_col = int(input(f"Player {player} chooses col: "))
        if self.board[player_row][player_col] == '-':
            if player == 1:
                player_sign = self.p1_sign
            elif player == 2:
                player_sign = self.p2_sign

            self.board[player_row][player_col] = player_sign
            TicTacToe.draw_board(self)
        else:
            TicTacToe.go(self,player)


    def check_draw(self):
        for row in self.board:
            for col in row:
                if col == '-':
                    return False


    def check_row(self, player):
        for row in self.board:
            if len(set(row)) == 1:
                if player == 1 and row[0] == self.p1_sign:
                    return True
                elif player == 2 and row[0] == self.p1_sign:
                    return True


    def check_col(self, player):
        for col in range(3):
            check_list = []
            for row in range(3):
                check_list.append(self.board[row][col])
            
            if len(set(check_list)) == 1:
                if player == 1 and check_list[0] == self.p1_sign:
                    return True
                elif player == 2 and check_list[0] == self.p1_sign:
                    return True


                
    def check_diagonal(self, player):
        check_list = [self.board[0][0], 
                    self.board[1][1],
                    self.board[2][2]]
        if len(set(check_list)) == 1:
            if player == 1 and check_list[0] == self.p1_sign:
                return True
            elif player == 2 and check_list[0] == self.p1_sign:
                return True
        
        check_list = [self.board[0][2], 
                    self.board[1][1],
                    self.board[2][0]]
        if len(set(check_list)) == 1:
            if player == 1 and check_list[0] == self.p1_sign:
                return True
            elif player == 2 and check_list[0] == self.p1_sign:
                return True


if __name__ == "__main__":
    game = TicTacToe()
    game.draw_board()
    game.choose_player()
    
    while True:
        while True:
            game.go(1)
            if game.check_draw():
                print("Draw")
                break
            elif game.check_row(1) or game.check_col(1) or game.check_diagonal(1):
                print("Player 1 has won")
                break

            game.go(2)
            if game.check_draw():
                print("Draw")
                break
            elif game.check_row(2) or game.check_col(2) or game.check_diagonal(2):
                print("Player 2 has won")
                break
        
        answer = input("Do you want to play again (y/n): ")
        if answer == 'n':
            break
        
