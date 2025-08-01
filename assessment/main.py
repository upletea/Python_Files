# import libraries

from data import *
from functions import clear_screen 

from colorama import init, Fore, Style
init(autoreset=True)  # Resets colour after each print

#debug
clear_screen()
print(rooms)
print(room_text)


# set up variables
ALIVE=True
PLAYER_LOC=rooms[1]
print(PLAYER_LOC)



# main game loop

def main():
  """Main Game Loop"""

print(Fore.YELLOW + "You are in the ARMOURY.")
print(Fore.CYAN + "You see: blaster")
print(Fore.RED + "You can't go that way.")
print("=" * 50)
print("              THE ELEMENTAL TRIALS")
print("=" * 50)

# while ALIVE:


#loc 1


# if dead BREAK
# or if win BREAK

#loc 2