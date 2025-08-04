# import libraries


from data import *
from functions import clear_screen, exit_game, restart_level 

#debug
clear_screen()
#print(rooms)
#print(room_text)


# set up variables
#ALIVE=True
#PLAYER_LOC=rooms[1]
#print(PLAYER_LOC)



# main game loop

def main():
  """Main Game Loop"""

print("=" * 50)
print("              THE ELEMENTAL TRIALS")
print("=" * 50)

inventory = []
player_health = 100
turn_count = 0
game_map = 


# while ALIVE:


#loc 1
PLAYER_LOC = rooms(0)
print(PLAYER_LOC)
print(rooms_text)[0]

# if dead BREAK
# or if win BREAK

#loc 2
PLAYER_LOC = rooms(1)
print(PLAYER_LOC)
print(rooms_text)[1]

#loc 3
PLAYER_LOC = rooms(2)
print(rooms_text)[2]
game_map = [
    ["Festive Field", "Freaky Forest", ""],
    ["Fabulous Farm", "Valiant Village", "Radical River"],
    ["Majestic Mountains", "Curble's Campsite", "Tasty Tower"]
]

location_descriptions = {
    "Festive Field": "Where the trees twinkle year-round, the air smells suspiciously like cinnamon, and even the squirrels know how to conga.",
    "Freaky Forest": "Where the trees whisper your secrets, the mushrooms giggle when you step on them, and the raccoons organize weekly séances.",
    "Fabulous Farm": "Where the cows strut like runway models, the corn wears sequins, and every sunrise comes with a disco ball.",
    "Valiant Village": "Where every grandma wields a sword, the chickens patrol in armor, and the town meetings end with epic boss battles.",
    "Radical River": "Where the water surfs itself, the fish wear shades, and even the otters say 'cowabunga' before doing backflips off the rocks.",
    "Majestic Mountains": "Where the cliffs sing opera at dawn, snowflakes sparkle like glitter bombs, and yetis run a five-star hot cocoa spa.",
    "Curble's Campsite": "The only place where you might roast marshmallows, dodge flying raccoons, and accidentally ignite your sleeping bag—all before breakfast.",
    "Tasty Tower": "A dangerously delicious skyscraper where each floor is a new flavor, the elevators run on whipped cream, and one wrong bite could trigger a fondue flood."
}


directions = {
    "N": (-1, 0),  # North → up
    "S": (1, 0),   # South → down
    "E": (0, 1),   # East → right
    "W": (0, -1)   # West → left
}

def show_map(pos):
    for i in range(3):
        row = ""
        for j in range(3):
            if (i, j) == pos:
                row += "[X] "
            elif game_map[i][j]:
                row += "[O] "
            else:
                row += " .  "
        print(row)
    print()

def get_moves(pos):
    moves = []
    for d, (dx, dy) in directions.items(): #d is just the counter
        x, y = pos[0] + dx, pos[1] + dy
        if 0 <= x < 3 and 0 <= y < 3 and game_map[x][y]:
            moves.append(d)
    return moves

def play():
    pos = (0, 0)  # Start at Emond's Field
    print("Your quest is to reach the Tasty Tower!\n")
    while True:
        show_map(pos)
        place = game_map[pos[0]][pos[1]]
        print("You are at:", place)
        print(location_descriptions[place])

        if place == "Tasty Tower":
            print("You reached the Tasty Tower! You win!")
            break

        moves = get_moves(pos)
        print("Available moves:", moves)

        move = input("Move (N/S/E/W): ").upper()
        if move in moves:
            dx, dy = directions[move]
            pos = (pos[0] + dx, pos[1] + dy)
        else:
            print("Invalid move. Try again.\n")
            

play()



#loc 4
PLAYER_LOC = rooms(3)
print(PLAYER_LOC)
print(rooms_text)[3]

inventory.append( "dog thingy")

print("_this is the riddle")

print("_option a_")
print("_option b_")
print("_option c_")
print("_option d_")

RiddleInput = input("Enter the correct answer: (A/B/C/D)")

if RiddleInput == ("C"):
   print("You have completed the Inferno Trial!")
else:
   resetOrQuit = input("You have failed to escape from the fire.  Press A to reset level or B to quit the game")
   
while True:
    resetOrQuit = input("You have failed to escape from the fire. Press A to reset level or B to quit the game: ")
    if resetOrQuit == "A":
        exit_game()
        break
    elif resetOrQuit == "B":
        restart_level()
        break
    else:
        print("Invalid input. Please enter A or B.")

#loc 5
PLAYER_LOC = rooms(4)
print(PLAYER_LOC)
print(rooms_text)[4]
#loc 6
PLAYER_LOC = rooms(5)
print(PLAYER_LOC)
print(rooms_text)[5]

#loc 7
PLAYER_LOC = rooms(6)
print(PLAYER_LOC)
print(rooms_text)[6]
 
 #List the weapons and special attacks
weapons = ["Firing Squad", "Rifle", "Grenade"]
special_attacks = ["Incinerate", "Poison", "Paralyse"]
enemies = ["Casual Curtis", "Scary Sienna", "Aggressive Aapti", "Killer Keira" ]

# Set the player's health to 100 and the enemy's health to 90
player_health = 100 
enemy_health = 90

print(f"You have {len(weapons)} Weapons:", weapons)
print(f"You have {len(special_attacks)} Special Attacks:", special_attacks)
print(f"You have {len(enemies)} Enemy Options:", enemies)

# Gives the user options to change their list of weapons
print("\n Weapon Management ")
print("1. Add a new weapon")
print("2. Remove a weapon")
print("3. Continue to battle")

# .split().lower() makes sure user can input the response with a lowercase letter
weapon_choice = input("Choose an option (1, 2, or 3): ") 
# If they chose to add a weapon...
if weapon_choice == "1":
        # It asks them what weapon they want to add
        new_weapon = input("Enter the name of the weapon to add: ")
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
    print("Continuing to battle!")

# Displays new weapon choices and continue the battle as usual
print(f"You have {len(weapons)} weapons:", weapons)

# Show the player the health of them and their oponent
print(f"Your health: {player_health}")
print(f"Enemy health: {enemy_health}")

# This loop will run while both the player's health and the enemy's health is more than 0
while player_health > 0 and enemy_health > 0:
    # This will ask them what their weapon of choice and attack style is
    weapon = input("Choose your weapon: ") 
    attack = input("Choose your special attack: ")
    enemy = input("CHoose what enemy you would like to face: ") 
    # If they choose the firing squad...
    if weapon == "Firing Squad":
        # Set the damage for the particular weapon
        damage = 35
        # Use subtraction to create the new enemy_health
        enemy_health = enemy_health - damage
        # Display to the user what they used and how much damage it dealth
        print(f"You attack with {weapon} and deal {damage} damage.")
        # Display what the enemy's new health is
        print(f"Enemy health:", {enemy_health})

        # Start the enemy's turn
        print("Enemy's turn")
        # Use the damage dealt from the enemy to work out the player's new health
        # decide which enemy gives a particular amount of damage
        if enemy == "Casual Curtis":
            enemy_damage = 15
        elif enemy == "Scary Sienna":
            enemy_damage = 20
        elif enemy == "Aggressive Aapti":
            enemy_damage = 25
        elif enemy == "Killer Keira":
            enemy_damage = 30
        else:
            print("Invalid choice!")
        player_health = player_health - enemy_damage
        # Display to the player their new stats
        print(f"Enemy attacks you for: {enemy_damage} damage!")
        print(f"Your health: {player_health}") 

    # If they choose the rifle...
    elif weapon == "Rifle":
        # Set the damage for the particular weapon 
        damage = 15
        # Use subtraction to create the new enemy_health
        enemy_health = enemy_health - damage
        # Display to the user what they used and how much damage it dealth
        print(f"You attack with {weapon} and deal {damage} damage.")
        # Display what the enemy's new health is
        print(f"Enemy health: {enemy_health}") 

        # Start the enemy's turn
        print("Enemy's turn")
        # Use the damage dealt from the enemy to work out the player's new health
        # decide which enemy gives a particular amount of damage
        if enemy == "Casual Curtis":
            enemy_damage = 15
        elif enemy == "Scary Sienna":
            enemy_damage = 20
        elif enemy == "Aggressive Aapti":
            enemy_damage = 25
        elif enemy == "Killer Keira":
            enemy_damage = 30
        else:
            print("Invalid choice!")
        player_health = player_health - enemy_damage
        # Display to the player their new stats
        print(f"Enemy attacks you for: {enemy_damage} damage!")
        print(f"Your health: {player_health}")


    # If they choose the grenade...
    elif weapon == "Grenade":
        # Set the damage for the particular weapon 
        damage = 25
        # Use subtraction to create the new enemy_health
        enemy_health = enemy_health - damage
        # Display to the user what they used and how much damage it dealth
        print(f"You attack with {weapon} and deal {damage} damage.")
        # Display what the enemy's new health is
        print(f"Enemy health: {enemy_health}")

        # Start the enemy's turn
        print("Enemy's turn")
        # Use the damage dealt from the enemy to work out the player's new health
        # decide which enemy gives a particular amount of damage
        if enemy == "Casual Curtis":
            enemy_damage = 15
        elif enemy == "Scary Sienna":
            enemy_damage = 20
        elif enemy == "Aggressive Aapti":
            enemy_damage = 25
        elif enemy == "Killer Keira":
            enemy_damage = 30
        else:
            print("Invalid choice!")
        player_health = player_health - enemy_damage
        # Display to the player their new stats
        print(f"Enemy attacks you for: {enemy_damage} damage!")
        print(f"Your health: {player_health}")

    # If they choose their new weapon...
    elif weapon == new_weapon:
        # Set the damage for the particular weapon 
        damage = int(input("How much damage does your new weapon do? Make sure that it is less that 50."))
        # Use subtraction to create the new enemy_health
        enemy_health = enemy_health - damage
        # Display to the user what they used and how much damage it dealth
        print(f"You attack with {new_weapon} and deal {damage} damage.")
        # Display what the enemy's new health is
        print(f"Enemy health: {enemy_health}")

        # Start the enemy's turn
        print("Enemy's turn")
        # Use the damage dealt from the enemy to work out the player's new health
        # Decide which enemy gives a particular amount of damage
        if enemy == "Casual Curtis":
            enemy_damage = 15
        elif enemy == "Scary Sienna":
            enemy_damage = 20
        elif enemy == "Aggressive Aapti":
            enemy_damage = 25
        elif enemy == "Killer Keira":
            enemy_damage = 30
        else:
            print("Invalid choice!")
        player_health = player_health - enemy_damage
        # Display to the player their new stats
        print(f"Enemy attacks you for: {enemy_damage} damage!")
        print(f"Your health: {player_health}")


    else:
        # If the player does not put in one of the set options, it will get them to go again
        print("Invalid choice! You miss your turn.") 
    # Once the enemy's score is zero or below, the loop will break
    if enemy_health <= 0:
        break

# If the player's health is over 0, then they will have won the game
if player_health > 0:
    print("You win the battle!")
# If the player's health is less than 0, then they will have lost the game
else:
    print("You have been defeated.")



 
