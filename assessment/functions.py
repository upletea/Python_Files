import os
import random
import colorama


from colorama import init, Fore, Style, Back
init(autoreset=True)  # Resets colour after each print

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_game():
    os._exit(1)

def restart_level():
   global player, score, exit_game
   player.reset_position()
   score = 0
   exit_game = False



