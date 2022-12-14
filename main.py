import colorama
from player import Player
from board import Board
from game import Game

colorama.init(autoreset=True)
HEIGHT = 7
WIDTH = 7
SEQUENCE_NEED = 5


def main():
    board = Board(HEIGHT, WIDTH)
    player1 = Player("", "X")
    player2 = Player("", "O")
    tic_tac_toe_game = Game(board, player1, player2, SEQUENCE_NEED)
    tic_tac_toe_game.play()


if __name__ == "__main__":
    main()
