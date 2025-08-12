# import libraries

import random
from data import *
from functions import *

#debug



# set up variables
#ALIVE=True
#PLAYER_LOC=rooms[1]
#print(PLAYER_LOC)

# main game loop


def main():
  """Main Game Loop"""

print("=" * 50)
print(Style.NORMAL + Fore.MAGENTA + "               THE ELEMENTAL TRIALS")
print("=" * 50)
current_room = 0


#loc 0
def room_0():
    print(rooms_text[0])
    input("Press Enter to continue...")
    return True


#loc 1
def room_1():
    print(rooms_text[1])
    input("Press Enter to continue...")
    return True


#loc 2
def room_2():
    print(rooms_text[2])
    if play():  
        return True
    else:
        print("⚡CRACK!⚡ A flash of lightning strikes you, leaving you blinded and in tremendous pain. You struggle to stay conscious, but you can feel the life quickly seeping out of you. Too exhausted to cry for help, you accept your fate and let yourself slip into the depths of the unknown. GAME OVER.")
        return False


directions = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1)
}

# makes a 5x4 map with one lightning square per row
def generate_map():
    lightning_strike = []
    minigame_map = []
    for i in range(5):
        lightning_col = random.randint(0, 3)
        lightning_strike.append((i, lightning_col))
        row = []
        for j in range(4):
            if j == lightning_col:
                row.append("L")  # Lightning
            else:
                row.append("S")  # Safe
        minigame_map.append(row)
    return minigame_map, lightning_strike

# show the map
def show_minigame_map(pos, minigame_map):
    for i in range(5):
        row = ""
        for j in range(4):
            if (i, j) == pos:
                row += "[X] "
            elif minigame_map[i][j] == "L":
                row += "[!] "
            else:
                row += "[O] "
        print(row)
    print()

# get valid moves
def get_moves(pos):
    moves = []
    for d, (dx, dy) in directions.items():
        x, y = pos[0] + dx, pos[1] + dy
        if 0 <= x < 5 and 0 <= y < 4:
            moves.append(d)
    return moves

# checks if there is lightning
def is_lightningstrike(pos, minigame_map):
    return minigame_map[pos[0]][pos[1]] == "L"

# Game loop
def play():
    minigame_map, lightning_strike = generate_map()
    pos = (4, random.randint(0, 3))  #start at the south end
    print("A defined grid materializes infront of you. There is only one way to escape. You must get across. ")
    while True:
        show_minigame_map(pos, minigame_map)
        if is_lightningstrike(pos, minigame_map):
            print(Style.BRIGHT + Fore.CYAN + "⚡CRACK!⚡ A flash of lightning strikes you, leaving you blinded and in tremendous pain. You struggle to stay conscious, but you can feel the life quickly draining out of you. Too exhausted to cry for help, you accept your fate and let yourself slip into the depths of the unknown. GAME OVER.")
            break
        if pos[0] == 0:
            print("You have completed The Lightning Trial.")
            break
        moves = get_moves(pos)
        print("Available moves:", moves)
        move = input("Choose direction (N/S/E/W): ").upper()
        if move in moves:
            dx, dy = directions[move]
            pos = (pos[0] + dx, pos[1] + dy)
        else:
            print(Style.BRIGHT + Fore.RED + "You cannnot go in that direction. Please enter one of the available options.")

# Start the game
play()


#loc 3
PLAYER_LOC = rooms(3)
print(PLAYER_LOC)
print(rooms_text[3])
inventory.append( "dog thingy")

print("No legs have I to dance, No lungs have I to breathe, No life have I to live or die And yet I do all three. What am I?")

print("Wind")
print("Air")
print("Fire")
print("Water")

RiddleInput = input("Enter the correct answer: (A/B/C/D)").strip().lower()

if RiddleInput == ("C"):
   print("You have completed the first part of The Inferno Trial!")
else:
   resetOrQuit = input("You have failed to escape from the fire.  Press A to reset level or B to quit the game").strip().lower()
   
while True:
    resetOrQuit = input("You have failed to escape from the fire. Press A to reset level or B to quit the game: ").strip().lower()
    if resetOrQuit == "A":
        exit_game()
        break
    elif resetOrQuit == "B":
        restart_level()
        break
    else:
        print("Invalid input. Please enter A or B.")

print("I was carried into a dark room, and set on fire. I wept, and then my head was cut off. What am I?")

print("Wind")
print("A Candle")
print("Fire")
print("Water")

RiddleInput = input("Enter the correct answer: (A/B/C/D)").strip().lower()

if RiddleInput == ("B"):
   print("You have completed the Inferno Trial!")
else:
   resetOrQuit = input("You have failed to escape from the fire.  Press A to reset level or B to quit the game").strip().lower()
   
while True:
    resetOrQuit = input("You have failed to escape from the fire. Press A to reset level or B to quit the game: ").strip().lower()
    if resetOrQuit == "A":
        exit_game()
        break
    elif resetOrQuit == "B":
        restart_level()
        break
    else:
        print("Invalid input. Please enter A or B.")

#loc 4
PLAYER_LOC = rooms(4)
print(PLAYER_LOC)
print(rooms_text[4])
#loc 5
PLAYER_LOC = rooms(5)
print(PLAYER_LOC)
print(rooms_text[5])

#loc 6
PLAYER_LOC = rooms(6)
print(PLAYER_LOC)
print(rooms_text[6])
 
 #List the weapons and special attacks
print(f"You have {len(weapons)} Weapons:", weapons)
print(f"You have {len(special_attacks)} Special Attacks:", special_attacks)


# Gives the user options to change their list of weapons
print("\n Weapon Management ")
print("1. Add a new weapon")
print("2. Remove a weapon")
print("3. Continue to battle")

# .split().lower() makes sure user can input the response with a lowercase letter
weapon_choice = input("Choose an option (A, B, or C): ").strip().lower()
# If they chose to add a weapon...
if weapon_choice == "1":
        # It asks them what weapon they want to add
        new_weapon = input("Enter the name of the weapon to add: ").strip().lower()
        # Changes the list and adds the new weapon
        weapons.append(new_weapon)
        # Tells the user the new weapon was added
        print(f"{new_weapon} has been added to your arsenal.")
# If they chose to remove a weapon...
elif weapon_choice == "2":
        # It shows them their current weapons
        print("Current Weapons:", weapons)
        # Asks them what weapon they want to remove
        weapon_to_remove = input("Enter the name of the weapon to remove: ")
        if weapon_to_remove in weapons:
            weapons.remove(weapon_to_remove)
            print(f"{weapon_to_remove} has been removed.")
        else:
            print("That weapon is not in your list.")
elif weapon_choice == "3":
    print("Continuing to the Battle of the Elements")

# Displays new weapon choices and continue the battle as usual
print(f"You have {len(weapons)} weapons:", weapons)

# Show the player the health of them and their oponent
print(f"Your health: {player_health}")
print(f"Enemy health: {enemy_health}")

# This loop will run while both the player's health and the enemy's health is more than 0
while player_health > 0 and enemy_health > 0:
    # This will ask them what their weapon of choice and attack style is
    weapon = input("Choose your weapon: ").strip().lower()
    attack = input("Choose your special attack: ").strip().lower()
    print (enemy)

def battle():
    print(f"A {enemy} appears! Prepare for battle!")
    
    while enemy_health > 0 and player["health"] > 0:
        print(f"Your health: {player['health']}, {enemy}'s health: {enemy_health}")
        action = input("Do you want to (A)ttack or (H)eal? ").strip().lower()
        if action == "A":
            damage = random.choice(10, 30, 20, 15, 25, 35)
            enemy_health -= damage
            print(f"You dealt {damage} damage to the {enemy}.")
        elif action == "H":
            heal = random.choice(10, 20, 15, 5, 0, 25)
            player["health"] += heal
            print(f"You healed yourself for {heal} health.")
        else:
            print("Invalid action.")
        player_health = player_health - enemy_damage
        # Display to the player their new stats
        print(f"Enemy attacks you for: {enemy_damage} damage!")
        print(f"Your health: {player_health}") 

    if player["health"] > 0:
        print(f"You defeated  {enemy}!")
    else:
        print("You have been defeated. Game over.")
        exit()
        
        print("Enemy's turn")
       
        player_health = player_health - enemy_damage
       
        print(f"Enemy attacks you for: {enemy_damage} damage!")
        print(f"Your health: {player_health}")



       
        enemy_health = enemy_health - damage

        print(f"You attack with {weapon} and deal {damage} damage.")
        
        print(f"Enemy health: {enemy_health}")

      
main()





 



 
