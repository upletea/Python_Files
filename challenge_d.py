# List the weapons and special attacks
weapons = ["Firing Squad", "Rifle", "Grenade"]
special_attacks = ["Incinerate", "Poison", "Paralyse"]
enemies = ["Casual Curtis", "Scary Sienna", "Aggressive Aapti", "Killer Keira" ]

# Set the player's health to 100 and the enemy's health to 90
player_health = 100 
enemy_health = 90

# Display a starting message
print("Welcome, hero! You face an enemy in battle!")

# Show the player their weapon, enemy and attack options
# Also uses the len() function to show the length of each list
print(f"You have {len(weapons)} weapons:", weapons)
print(f"You have {len(special_attacks)} special Attacks:", special_attacks)
print(f"You have {len(enemies)} enemy options:", enemies)

# Gives the user options to change their list of weapons
print("\n Weapon Management ")
print("1. Add a new weapon")
print("2. Remove a weapon")
print("3. Continue to battle")

# . split.lower makes sure user can input the response with a lowercase letter
weapon_choice = input("Choose an option (1, 2, or 3): ").split().lower()
# If they chose to add a weapon...
if weapon_choice == "1":
        # It asks them what weapon they want to add
        new_weapon = input("Enter the name of the weapon to add: ").split().lower()
        # Changes the list and adds the new weapon
        weapons.append(new_weapon)
        # Tells the user the new weapon was added
        print(f"{new_weapon} has been added to your arsenal.")
# If they chose to remove a weapon...
elif weapon_choice == "2":
        # It shows them their current weapons
        print("Current Weapons:", weapons)
        # Asks them what weapon they want to remove
        weapon_to_remove = input("Enter the name of the weapon to remove: ").split().lower()
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
    weapon = input("Choose your weapon: ") .split().lower()
    attack = input("Choose your special attack: ") .split().lower()
    enemy = input("CHoose what enemy you would like to face: ") .split().lower()
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