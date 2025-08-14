# import libraries

import random
from data import *
from functions import *

#debug


def main():
  """Main Game Loop"""

print("=" * 50)
print(Style.BRIGHT + Fore.MAGENTA + "              THE ELEMENTAL TRIALS")
print("=" * 50)
current_room = 0
player_location = rooms[0]
print("Inventory:", inventory )
print("Health:",  player_health )
input("Press Enter to continue...")
clear_screen()

#loc 0
def room_0():
    print(Style.BRIGHT + Fore.LIGHTBLUE_EX + rooms[0])
    print(rooms_text[0])
    
    input("Press Enter to continue...")
    clear_screen()
    
    print("Looking at the array of doors eerily illuminated in front of you, you realise this is your fate."
          "Taking a deep breath, you slowly creep towards the closest room, carefully inspecting the dark oak door "
          "and admiring the intricate carving of a wave centred on it. Softly sighing in defeat, you reach out and twist the dull handle. "
          "A gust of wind sweeps you up, seemingly appearing from nowhere. Your vision blurs and you get swept into oblivion.")
    
    input("Press Enter to continue...")
    clear_screen()

player_location = rooms[1]
room_0()
clear_screen()

def room_1():
    print(Style.BRIGHT + Fore.LIGHTBLUE_EX + rooms[1])
    print(rooms_text[1])
    input("Press Enter to continue...")
    clear_screen()
    player_location = rooms[1]

    room_0()
    clear_screen()

room_1() 


while True:
    choice = input("Do you (A) try to find help, (B) run away, or (C) dive in yourself? ").strip().upper()
    clear_screen()

    if choice == "A":
        print("You sprint as fast as your legs carry you, screaming for help. No one appears. "
              "Getting more panicked, you see a small hut centred upon a hill. You bolt towards it, not looking back.")
        print("Huffing and panting, you finally reach the hut and...")
        break

    elif choice == "B":
        print("egb")
        print("gbe")
        break

    elif choice == "C":
        print("You fearlessly dive right into the violent waves filled with adrenaline, knowing that if you hadn't tried to save her, "
              "you would never be able to live with yourself.")
        print(Style.BRIGHT + Fore.CYAN + "~")
        print("You struggle through the water, coughing and wheezing as you get slammed from side to side. "
              "Looking up, you realise you were a lot closer than you anticipated. A large burst of energy envelops you, "
              "motivating you to push through the pain. With a final heave, you reach the drowning woman and tiredly reach to grasp her dainty hand.")
        print(Style.BRIGHT + Fore.CYAN + "~")
        print("You yank her towards you, choking on water as both you and her get sucked into the watery depths. "
              "With your deaths looming over you, a sense of dread falls upon you. Out of nowhere, an incredibly loud honk sounds. "
              "Wincing slightly, you glance around and notice a small rickety boat bobbing alone near you. You, along with the woman, "
              "paddle slowly towards it and scramble into it. Breathing a sigh of relief, you collapse onto the unsteady surface of the boat. You had survived.")
        
        input("Press Enter to continue...")
        clear_screen()
        
        print("Overwhelmed with gratitude, the woman reveals herself as a significant member of the Council of the Elements "
              "and presents you with an incredibly breathtaking stone, almost directly replicating the fierce nature of the sea. "
              "Your eyelids begin to feel heavy and you yawn involuntarily. Your eyes droop closed and....")
        
        clear_screen()
        inventory.append("Sea Stone")
        print("Item added to your inventory!", inventory)
        clear_screen()
        break

    else:
        print(Style.BRIGHT + Fore.RED + "Invalid input. Please enter A, B, or C.")


if choice not in ["A", "B", "C"]:
    while True:
        resetOrQuit = input("You failed to complete this Trial. Press A to reset level or B to quit the game: ").strip().upper()
        if resetOrQuit == "A":
            restart_level()
            break
        elif resetOrQuit == "B":
            exit_game()
            break
        else:
            print("Invalid input. Please enter A or B.")
    player_location = rooms[2]
    clear_screen()

#loc 2

directions = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1)
}
def room_2():
    print(Style.BRIGHT + Fore.LIGHTBLUE_EX + rooms[2])
    print(rooms_text[2])
    input("Press Enter to continue...")
    clear_screen()
    player_location = rooms[2]

    room_1()
    clear_screen()

room_2() 
def room_2():
    print(rooms_text[2])
    if play():  
        return True
    else:
        print("⚡CRACK!⚡ A flash of lightning strikes you, leaving you blinded and in tremendous pain. You struggle to stay conscious, but you can feel the life quickly seeping out of you. Too exhausted to cry for help, you accept your fate and let yourself slip into the depths of the unknown. GAME OVER.")
        return False

# Generate a 5x4 map with one random lightning square per row
def generate_map(): #used copilot to make the lightning_strike
    lightning_strike = []
    minigame_map = []
    for i in range(5):
        lightning_col = random.randint(0, 3)
        lightning_strike.append((i, lightning_col))
        row = []
        for j in range(4):
            if j == lightning_col:
                row.append("L")  # lightning
            else:
                row.append("S")  # safe
        minigame_map.append(row)
    return minigame_map, lightning_strike

# Show the map with hidden lightning
def show_minigame_map(pos, minigame_map):
    for i in range(5):
        row = ""
        for j in range(4):
            if (i, j) == pos:
                row += "[X] "
            else:
                row += "[O] "
        print(row)
    print()

# Reveal where the lightning was if they die
def reveal_map(minigame_map, pos):
    print("\n⚡ The grid crackles with electric fury, revealing the deadly path you failed to avoid:")
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

# Get valid moves
def get_moves(pos):
    moves = []
    for d, (dx, dy) in directions.items():
        x, y = pos[0] + dx, pos[1] + dy
        if 0 <= x < 5 and 0 <= y < 4:
            moves.append(d)
    return moves

# check if current position is lightning
def is_lightningstrike(pos, minigame_map):
    return minigame_map[pos[0]][pos[1]] == "L"

# game loop
def play():
    minigame_map, lightning_strike = generate_map()
    pos = (4, random.randint(0, 3))  # start at the south 
    print("A defined grid materializes in front of you. There is only one way to escape. You must get across.")
    
    while True:
        show_minigame_map(pos, minigame_map)
        
        if is_lightningstrike(pos, minigame_map):
            reveal_map(minigame_map, pos)
            print(Style.BRIGHT + Fore.CYAN + "⚡CRACK!⚡ A flash of lightning strikes you, leaving you blinded and in tremendous pain. You struggle to stay conscious, but you can feel the life quickly draining out of you. Too exhausted to cry for help, you accept your fate and let yourself slip into the depths of the unknown. GAME OVER.")
            return False
        
        if pos[0] == 0:
            print("🎉 You have completed The Lightning Trial.")
            return True
        
        moves = get_moves(pos)
        print("Available moves:", moves)
        move = input("Choose direction (N/S/E/W): ").upper()
        
        if move in moves:
            dx, dy = directions[move]
            pos = (pos[0] + dx, pos[1] + dy)
        else:
            print(Style.BRIGHT + Fore.RED + "You cannot go in that direction. Please enter one of the available options.")

# begin the game
room_2()
player_location = rooms[3]
clear_screen()
#loc 3
PLAYER_LOC = rooms(3)
print(PLAYER_LOC)
print(rooms_text[3])
rooms[3]

#part un
print("No legs have I to dance, No lungs have I to breathe, No life have I to live or die And yet I do all three. What am I?")

print("Wind (A)")
print("Air (B)")
print("Fire (C)")
print("A Flower (D)")

RiddleInput = input("Enter the correct answer: (A/B/C/D)").strip().upper()

if RiddleInput.strip().upper() == "C":
    print("You have completed the Inferno Trial!")
else:
    while True:
        resetOrQuit = input("You have failed to escape from the fire. Press A to reset level or B to quit the game: ").strip().upper()
        if resetOrQuit == "A":
            restart_level() 
            break
        elif resetOrQuit == "B":
            exit_game()     
            break
        else:
            print("Invalid input. Please enter A or B.")


#part deux

print("I was carried into a dark room, and set on fire. I wept, and then my head was cut off. What am I?")

print("Death (A)")
print("A Candle (B)")
print("Fire (C)")
print("An Infant (D)")

RiddleInput = input("Enter the correct answer: (A/B/C/D)").strip().upper()

if RiddleInput.strip().upper() == "B":
    print("You have completed the Inferno Trial!")
else:
    while True:
        resetOrQuit = input("You have failed to escape from the fire. Press A to reset level or B to quit the game: ").strip().upper()
        if resetOrQuit == "A":
            restart_level()  
            break
        elif resetOrQuit == "B":
            exit_game()      
            break
        else:
            print("Invalid input. Please enter A or B.")

#part trois

print("I am hewn from Earth and Fire; But to the sky, I aspire. I am nothing but contented; Until my patient rage is vented. What am I?")

print("A Therapist (A)")
print("A Volcano (B)")
print("Fire (C)")
print("Water (D)")

RiddleInput = input("Enter the correct answer: (A/B/C/D)").strip().upper()

if RiddleInput.strip().upper() == "B":
    print("You have completed the Inferno Trial!")
    inventory.append()
else:
    while True:
        resetOrQuit = input("You have failed to escape from the fire. Press A to reset level or B to quit the game: ").strip().upper()
        if resetOrQuit == "A":
            restart_level() 
            break
        elif resetOrQuit == "B":
            exit_game()    
            break
        else:
            print("Invalid input. Please enter A or B.")

clear_screen()
rooms[3]

#loc 4
PLAYER_LOC = rooms(4)
print(PLAYER_LOC)
print(rooms_text[4])

#loc 5
PLAYER_LOC = rooms(5)
print(PLAYER_LOC)
print(rooms_text[5])
 
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
if weapon_choice == "a":
        # It asks them what weapon they want to add
        new_weapon = input("Enter the name of the weapon to add: ").strip().lower()
        # Changes the list and adds the new weapon
        weapons.append(new_weapon)
        # Tells the user the new weapon was added
        print(f"{new_weapon} has been added to your arsenal.")
# If they chose to remove a weapon...
elif weapon_choice == "b":
        # It shows them their current weapons
        print("Current Weapons:", weapons)
        # Asks them what weapon they want to remove
        weapon_to_remove = input("Enter the name of the weapon to remove: ")
        if weapon_to_remove in weapons:
            weapons.remove(weapon_to_remove)
            print(f"{weapon_to_remove} has been removed.")
        else:
            print("That weapon is not in your list.")
elif weapon_choice == "c":
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
            damage = random.choice([10, 15, 25])
            enemy_health -= damage
            print(f"You dealt {damage} damage to the {enemy}.")
        elif action == "H":
            heal = random.choice([10, 20, 5])
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





 
