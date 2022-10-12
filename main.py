import os
import colorama
from colorama import Fore, Back, Style
from Player import Player
from Board import Board

colorama.init(autoreset=True)

HEIGHT = 7
WIDTH = 7
SEQUENCE_NEED = 5
X = 'X'
O = 'O'


def main():
    welcome()
    board = Board(HEIGHT, WIDTH)
    player1 = Player(input("First player name: "), X)
    player2 = Player(input("Second player name: "), O)
    who_is_turn = player1
    welcome()
    board.printBoard()
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

        while not board.placeIsValid(player_choice // HEIGHT, player_choice % WIDTH):
            print("Wrong input or place is already taken.")
            player_choice = input("Move > ")
            while not player_choice.isdecimal():
                print("Wrong input or place is already taken.")
                player_choice = input("Move > ")

            player_choice = int(player_choice)

        welcome()

        board.updateBoard(player_choice // HEIGHT, player_choice % WIDTH, who_is_turn.getSymbol())

        board.printBoard()

        # Check if someone won after the last move
        if checkIfWin(board, player_choice // HEIGHT, player_choice % WIDTH, who_is_turn.getSymbol()):
            welcome()
            board.printBoard()
            print(
                Back.WHITE + Fore.BLACK + f"\nThe winner is {who_is_turn.getSymbol()} ! \nWell Done {who_is_turn.getName()} ")
            goodBye()
            break

        # Check if Tie
        if board.boardIsFull():
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
    for element in board.getRow(x):
        if element == symbol:
            sequence += 1
        else:
            sequence = 0
        if sequence >= SEQUENCE_NEED:
            return True
    return False


def checkIfColWin(board, y, symbol):
    sequence = 0
    for element in board.getCol(y):
        if element == symbol:
            sequence += 1
        else:
            sequence = 0
        if sequence >= SEQUENCE_NEED:
            return True
    return False


def checkIfLeftDiagonalWin(board, x, y, symbol):
    sequence = 0
    for element in board.getLeftDiagonal(x, y):
        if element == symbol:
            sequence += 1
        else:
            sequence = 0
        if sequence >= SEQUENCE_NEED:
            return True
    return False


def checkIfRightDiagonalWin(board, x, y, symbol):
    sequence = 0
    for element in board.getRightDiagonal(x, y):
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
