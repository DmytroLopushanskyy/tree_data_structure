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
        print("Your mark is \"⭕\".\nExample board demonstrating correct indexes:")
        print(self.example_board)
        while True:
            try:
                inp = int(input("Please enter ONE DIGIT where you want to place your mark: "))
                self.board.place(inp, "⭕")
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
                self.board.take_turn()
                print(self.board)
                status = self.board.check_status()
                if status[0] == "finished":
                    if status[1] == self.board.first_player:
                        print("Congratulations! You won the game!")
                    elif status[1] == self.board.second_player:
                        print("You lost the game! Try one more time!")
                    else:
                        print("It is a draw!")
                    break


if __name__ == '__main__':
    GAME = TicTacToe()
    GAME.start()
