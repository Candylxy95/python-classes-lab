class Game:
    def __init__(self, turn = 'X', tie = False, winner = False):
        self.tie = tie
        self.winner = winner
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
            }
        self.turn = turn

    def play_game(self):
        print(f'Welcome to TIC TAC TOE')
        while True:
            if self.winner or self.tie:
                self.print_board()
                self.print_message()
                if self.play_again() == 'y':
                    self.reset_game()
                else: break
            self.print_board()
            self.print_message()
            player_move = self.get_move()
            self.place_piece(player_move, self.turn)
            self.check_for_winner()
            self.check_for_tie()
            self.switch_move()





    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
          """)

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"Player '{self.turn}' wins the game")
        else:
            print(f'It is currently player {self.turn}\'s turn.')

    def switch_move(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'


    def get_move(self):
        while True:
            move = input(f'Enter a valid move (example: A1): ').lower()
            if move not in self.board or self.board[move]:
                print("Invalid move. Please try again")
            else: return move

    def place_piece(self, move, turn):
            self.board[move] = turn

    def check_for_winner(self):
        winning_combinations = [
            ["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"],
            ["a1", "b1", "c1"], ["a2", "b2", "c2"], ["a3", "b3", "c3"],
            ["a1", "b2", "c3"], ["a3", "b2", "c1"]
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] and self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]:
                self.winner = True

    def check_for_tie(self):
        for key in self.board:
            if self.board[key] is not None and self.winner == False:
                self.tie = True
            else:
                self.tie = False

    def play_again(self):
        return input("Game has ended! Enter 'y' to play again. ").lower()


    def reset_game(self):
            self.tie = False
            self.winner = False
            self.board = {
                'a1': None, 'b1': None, 'c1': None,
                'a2': None, 'b2': None, 'c2': None,
                'a3': None, 'b3': None, 'c3': None,
            }
            self.turn = 'X'



game_instance = Game()
game_instance.play_game()
