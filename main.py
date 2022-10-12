import os
import colorama
from colorama import Fore, Back, Style
from Player import Player
from Board import Board

colorama.init(autoreset=True)

HEIGHT = 4
WIDTH = 4
SEQUENCE_NEED = 2
X = 'X'
O = 'O'


def main():
    welcome()
    board = Board(HEIGHT, WIDTH)
    player1 = Player(input("First player name: "), X)
    player2 = Player(input("Second player name: "), O)
    who_is_turn = player1
    welcome()
    board.print_board()
    while True:
        print()
        print(f'Current player symbol: {who_is_turn.getSymbol()}')
        print(f'Current player name: {who_is_turn.getName()}')
        print()
        player_choice = input("Move > ")
        while not player_choice.isdecimal():
            print("Wrong input or place is already taken.")
            player_choice = input("Move > ")
        player_choice = int(player_choice)

        while not board.is_place_valid(player_choice // HEIGHT, player_choice % WIDTH):
            print("Wrong input or place is already taken.")
            player_choice = input("Move > ")
            while not player_choice.isdecimal():
                print("Wrong input or place is already taken.")
                player_choice = input("Move > ")

            player_choice = int(player_choice)

        welcome()

        board.update_board(player_choice // HEIGHT, player_choice % WIDTH, who_is_turn.getSymbol())

        board.print_board()

        # Check if someone won after the last move
        if checkIfWin(board, player_choice // HEIGHT, player_choice % WIDTH, who_is_turn.getSymbol()):
            welcome()
            board.print_board()
            print(
                Back.WHITE + Fore.BLACK + f"\nThe winner is {who_is_turn.getSymbol()} ! \nWell Done {who_is_turn.getName()} ")
            goodBye()
            break

        # Check if Tie
        if board.is_board_full():
            print("Tie Game! ")
            goodBye()
            break

        # Change the turn for the next player
        who_is_turn = switchTurn(who_is_turn, player1, player2)


def checkIfWin(board, x, y, symbol):
    if checkIfRowWin(board, x, symbol) or checkIfColWin(board, y, symbol):
        return True
    if checkIfLeftDiagonalWin(board, x, y, symbol) or checkIfRightDiagonalWin(board, x, y, symbol):
        return True
    return False


def checkIfRowWin(board, x, symbol):
    sequence = 0
    for element in board.get_row(x):
        if element == symbol:
            sequence += 1
        else:
            sequence = 0
        if sequence >= SEQUENCE_NEED:
            return True
    return False


def checkIfColWin(board, y, symbol):
    sequence = 0
    for element in board.get_col(y):
        if element == symbol:
            sequence += 1
        else:
            sequence = 0
        if sequence >= SEQUENCE_NEED:
            return True
    return False


def checkIfLeftDiagonalWin(board, x, y, symbol):
    sequence = 0
    for element in board.get_left_diagonal(x, y):
        if element == symbol:
            sequence += 1
        else:
            sequence = 0
        if sequence >= SEQUENCE_NEED:
            return True
    return False


def checkIfRightDiagonalWin(board, x, y, symbol):
    sequence = 0
    for element in board.get_right_diagonal(x, y):
        if element == symbol:
            sequence += 1
        else:
            sequence = 0
        if sequence >= SEQUENCE_NEED:
            return True
    return False


def switchTurn(who_is_turn, player1, player2):
    if who_is_turn == player1:
        return player2
    return player1


def welcome():
    os.system("clear")
    print(Back.GREEN + Fore.BLACK + " WELCOME TO THE GAME OF TIC-TAC-TEO \n")


def goodBye():
    print("\nThanks for playing my TIC-TAC-TEO game!")
    print("See you next time.\n")


if __name__ == '__main__':
    main()
