"""
Tic Tac Toe Game Interface
"""
from board import Board, OccupiedError


class TicTacToe:
    """
    Main game class
    """
    def __init__(self):
        """
        Game initialisation.
        """
        self.board = Board()
        self.example_board = Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def start(self):
        """
        Start game.
        """
        while True:
            try:
                role = int(input("Please input which player you want to be. 1 or 2: "))
                if not 1 <= role <= 2:
                    print("Wrong value. Please input 1 or 2.")
                    continue
                break
            except ValueError:
                print("Wrong value. Please input 1 or 2.")
        if role == 1:
            mark = self.board.first_player
            self.board.human_player = self.board.first_player
            self.board.automated_player = self.board.second_player
        else:
            mark = self.board.second_player
            self.board.automated_player = self.board.first_player
            self.board.human_player = self.board.second_player
        print("Your mark is %s.\nExample board demonstrating correct indexes:" % mark)
        print(self.example_board)
        while True:
            try:
                if role != 2:
                    inp = int(input("Please enter ONE DIGIT where you want to place your mark: "))
                    self.board.place(inp, mark)
                else:
                    role += 1
            except OccupiedError:
                print("The place at index %s is already occupied! Try "
                      "one more time!" % inp)
            except IndexError:
                print("Wrong index. Please provide a number in 1-9 range")
            except ValueError:
                continue
            except KeyboardInterrupt:
                break
            else:
                if self.status():
                    break

                if role == 3:
                    # first decision, takes lots of time.
                    print("Plase wait 10 seconds. Computer is making a hard decision.")

                self.board.take_turn()
                print(self.board)

                if self.status():
                    break

    def status(self):
        """
        Checks board status. Returns True if the game is over.
        """
        status = self.board.check_status()
        if status[0] == "finished":
            if status[1] == self.board.human_player:
                print("Congratulations! You won the game!")
            elif status[1] == self.board.automated_player:
                print("You lost the game! Try one more time!")
            else:
                print("It is a draw!")
            return True
        if self.board.is_full():
            print(self.board)
            print("It is a draw!")
            return True
        return False


if __name__ == '__main__':
    GAME = TicTacToe()
    GAME.start()
