import random

class Game:
    def __init__(self):
        self.board = [[" "] * 3 for i in range(3)]
        while True:
            choice = input("Player 1 Choose X or O: ").upper()
            if choice in ["X", "O"]:
                break
            print("Invalid input! Please enter X or O.")

        if choice == "X":
            self.playersym = "X"
            self.botsym = "O"
        else:
            self.playersym = "O"
            self.botsym = "X"

        self.current = self.playersym

    def reset_board(self):
        self.board = [[" "] * 3 for i in range(3)]
        self.current = self.playersym

    def show_board(self):
        for row in self.board:
            print(" | ".join(row))
            print('-' * 9)
    
    def win_check(self):
        if self.board[0][0] == self.board [1][1] == self.board[2][2] != " " :
            return self.board[0][0]
        
        if self.board[0][2] == self.board [1][1] == self.board[2][0] != " " :
            return self.board[0][2]
        
        for row in self.board:
            if row[0] == row[1] == row[2] != " " :
                return row[0]
            
        for col in range(3) :
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " " :
                return self.board[0][col]
            
        return None

    def move_left(self):
        for row in self.board:
            if row[0] == " " or row[1] == " " or row[2] == " " :
                return True
        return False
    
    def player(self) :
        while True:
            self.show_board()
            try:
                move = int(input(f"Player {self.current}, Enter Your Move (1-9): "))
                if not 1 <= move <= 9:
                    print("Invalid move! Please enter a number between 1 and 9.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            row = (move-1)//3
            col = (move-1)%3

            if self.board[row][col] != " " :
                print("Invalid Move!")
            else:
                self.board[row][col] = self.current
                break
    
    def Eval(self,playersym,compsym) :
        winner = self.win_check()

        if winner == playersym:
            return -10
        elif winner == compsym:
            return 10
        else :
            return 0
        
    def easy(self):
        while True:
            move = random.randint(1,9)
            row = (move-1)//3
            col = (move-1)%3

            if self.board[row][col] == " " :
                self.board[row][col] = self.current
                break
    
    def medium(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = self.current
                    if self.win_check() == self.current:
                        return
                    self.board[i][j] = " "

        opponent = "X" if self.current == "O" else "O"
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = opponent
                    if self.win_check() == opponent:
                        self.board[i][j] = self.current
                        return
                    self.board[i][j] = " "

        self.easy()

    def minimax(self,depth,isMax):

        score = self.Eval(self.playersym,self.botsym)
        if score == 10:
            return score - depth
        elif score == -10:
            return score + depth
        elif not self.move_left():
            return 0
        
        if isMax :
            best = -1000

            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = self.botsym
                        value = self.minimax(depth+1,False)
                        if value > best :
                            best = value
                        self.board[i][j] = " "

            return best
                    
        if not isMax :
            best = 1000

            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = self.playersym
                        value = self.minimax(depth+1,True)
                        if value < best :
                            best = value
                        self.board[i][j] = " "

            return best
        
    def hard(self):
        bestVal = -1000
        bestMove = (-1,-1)

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = self.botsym
                    moveVal = self.minimax(0,False)
                    self.board[i][j] = " "

                    if moveVal > bestVal:
                        bestMove = (i,j)
                        bestVal = moveVal

        self.board[bestMove[0]][bestMove[1]] = self.botsym
        
    def game_loop(self, bot_function = None):
        while True:

            if bot_function == None:
                self.player()
            else :
                if self.current == self.playersym:
                    self.player()
                else:
                    bot_function()

            win = self.win_check()
            if win :
                self.show_board()
                print(f"Winner is player {win}")
                break
            elif not self.move_left() :
                self.show_board()
                print("Draw!")
                break

            self.current = "O" if self.current == "X" else "X"

                    
def Instruct():
    print("Welcome to Tic-Tac-Toe!")
    print("Players take turns entering a number (1-9) to place their symbol (X or O).")
    print("The board positions are as follows:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print("Let the game begin!\n")

def main():
    Instruct()
    game = Game()

    while True:
        print("Who do you wanna play with?")
        print("1.Player\n2.Computer")
        while True:
            try:
                ch = int(input("Enter Your Choice (1-2): "))
                if ch in [1, 2]:
                    break
                print("Invalid choice! Please enter 1 or 2.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        if ch == 1 :
            game.game_loop()
        if ch == 2 :
            print("Select Difficulty")
            print("1.Easy\n2.Medium\n3.Hard")
            while True:
                try:
                    choice = int(input("Enter Your Choice (1-3): "))
                    if choice in [1, 2, 3]:
                        break
                    print("Invalid choice! Please enter 1, 2, or 3.")
                except ValueError:
                    print("Invalid input! Please enter a number.")

            if choice == 1 :
                game.game_loop(game.easy)
            elif choice == 2:
                game.game_loop(game.medium)
            elif choice == 3:
                game.game_loop(game.hard)

        play_again = input("\nPlay Again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break
        game.reset_board()

if __name__ == "__main__" :
    main()