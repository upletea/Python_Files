# List the weapons and special attacks
weapons = ["Firing Squad", "Rifle", "Grenade"]
special_attacks = ["Incinerate", "Poison", "Paralyse"]
enemies = ["Casual Curtis", "Scary Sienna", "Agressive Aapti", "Killer Keira" ]

# Set the player's health to 100 and the enemy's health to 90
player_health = 100 
enemy_health = 90

# Display a starting message
print("Welcome, hero! You face an enemy in battle!")

# Show the player their weapon, enemy and attack options
print("Your Weapons:", weapons)
print("Your Special Attacks:", special_attacks)
print("Your enemy options:", enemies)

# Show the player the health of them and their oponent
print("Your health:",{player_health})
print("Enemy health:",{enemy_health})

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
        print(f"You attack with", {weapon}, "and deal", {damage}, "damage.")
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
        print("Enemy attacks you for:", enemy_damage, "damage!")
        print("Your health:",{player_health})

    # If they choose the rifle...
    elif weapon == "Rifle":
        # Set the damage for the particular weapon 
        damage = 15
        # Use subtraction to create the new enemy_health
        enemy_health = enemy_health - damage
        # Display to the user what they used and how much damage it dealth
        print(f"You attack with", {weapon}, "and deal", {damage}, "damage.")
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
        print("Enemy attacks you for:", enemy_damage, "damage!")
        print("Your health:",{player_health})


    # If they choose the grenade...
    elif weapon == "Grenade":
        # Set the damage for the particular weapon 
        damage = 25
        # Use subtraction to create the new enemy_health
        enemy_health = enemy_health - damage
        # Display to the user what they used and how much damage it dealth
        print(f"You attack with", {weapon}, "and deal", {damage}, "damage.")
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
        print("Enemy attacks you for:", enemy_damage, "damage!")
        print("Your health:",{player_health})


    else:
        # If the player does not put in one of the set options, it will get them to go again
        print("Invalid choice! You miss your turn.") 
    # Once the enemy's score is zero or below, the loop will break
    if enemy_health <= 0:
        break

# If the player's health is over 0, then they will have won the game
if player_health > 0:
    print("You win the battle")
# If the player's health is less than 0, then they will have lost the game
else:
    print("You have been defeated.")