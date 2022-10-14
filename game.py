import random
import os
from colorama import Fore, Back, Style


def print_welcome_game():
    os.system("clear")
    print(Back.GREEN + Fore.BLACK + " WELCOME TO THE GAME OF TIC-TAC-TEO \n")


def print_goodbye():
    print("\nThanks for playing my TIC-TAC-TEO game!")
    print("See you next time.\n")


class Game:
    def __init__(self, board, player1, player2, sequence_need=3):
        print_welcome_game()
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.player1.set_name(input("First player name: "))
        self.player2.set_name(input("Second player name: "))
        self.whose_turn_is_it = random.choice((player1, player2))
        self.sequence_need = sequence_need

    def play(self):
        print_welcome_game()
        self.board.print_board()
        while True:
            print(f'Current player symbol: {self.whose_turn_is_it.get_symbol()}')
            print(f'Current player name: {self.whose_turn_is_it.get_name()}')
            player_choice = input("Move > ")

            player_choice = self.check_and_return_valid_choice(player_choice)

            print_welcome_game()

            self.board.update_board(player_choice // self.board.height, player_choice % self.board.width, self.whose_turn_is_it.get_symbol())

            self.board.print_board()

            # Check if someone won after the last move
            if self.check_if_win(player_choice // self.board.height, player_choice % self.board.width):
                print_welcome_game()
                self.board.print_board()
                print(
                    Back.WHITE + Fore.BLACK + f"\nThe winner is {self.whose_turn_is_it.get_symbol()} ! \nWell Done {self.whose_turn_is_it.get_name()} ")
                print_goodbye()
                break

            # Check if Tie
            if self.board.is_board_full():
                print("Tie Game! ")
                print_goodbye()
                break

            self.switch_turn()

    def check_and_return_valid_choice(self, player_choice):
        while not player_choice.isdecimal():
            print("Wrong input or place is already taken.")
            player_choice = input("Move > ")
        player_choice = int(player_choice)
        while not self.board.is_place_valid(player_choice // self.board.height, player_choice % self.board.width):
            print("Wrong input or place is already taken.")
            player_choice = input("Move > ")
            while not player_choice.isdecimal():
                print("Wrong input or place is already taken.")
                player_choice = input("Move > ")

            player_choice = int(player_choice)

        return player_choice

    def switch_turn(self):
        if self.whose_turn_is_it == self.player1:
            self.whose_turn_is_it = self.player2
        else:
            self.whose_turn_is_it = self.player1

    def check_if_win(self, x, y):
        if self.check_if_row_win(x) or self.check_if_col_win(y):
            return True
        if self.check_if_left_diagonal_win(x, y) or self.check_if_right_diagonal_win(x, y):
            return True
        return False

    def check_if_row_win(self, x):
        sequence = 0
        for element in self.board.get_row(x):
            sequence += 1 if element == self.whose_turn_is_it.get_symbol() else 0
            if sequence >= self.sequence_need:
                return True
        return False

    def check_if_col_win(self, y):
        sequence = 0
        for element in self.board.get_col(y):
            sequence += 1 if element == self.whose_turn_is_it.get_symbol() else 0
            if sequence >= self.sequence_need:
                return True
        return False

    def check_if_left_diagonal_win(self, x, y):
        sequence = 0
        for element in self.board.get_left_diagonal(x, y):
            sequence += 1 if element == self.whose_turn_is_it.get_symbol() else 0
            if sequence >= self.sequence_need:
                return True
        return False

    def check_if_right_diagonal_win(self, x, y):
        sequence = 0
        for element in self.board.get_right_diagonal(x, y):
            sequence += 1 if element == self.whose_turn_is_it.get_symbol() else 0
            if sequence >= self.sequence_need:
                return True
        return False
