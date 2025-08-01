import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

from colorama import init, Fore, Style
init(autoreset=True)  # Resets colour after each print