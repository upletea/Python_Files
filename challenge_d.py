# List the weapons and special attacks
weapons = ["Firing Squad", "Rifle", "Grenade"]
special_attacks = ["Incinerate", "Poison", "Paralyse"]

# Set the player's health to 100 and the enemy's health to 90
player_health = 100 
enemy_health = 90

# Display a starting message
print("Welcome, hero! You face an enemy in battle!")

# Show the player their weapon and attack options
print("Your Weapons:", weapons)
print("Your Special Attacks:", special_attacks)

# Show the player the health of them and their oponent
print("Your health:",{player_health})
print("Enemy health:",{enemy_health})

# This loop will run while both the player's health and the enemy's health is more than 0
while player_health > 0 and enemy_health > 0:
    # This will ask them what their weapon of choice and attack style is
    weapon = input("Choose your weapon: ")
    attack = input("Choose your special attack: ")
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
        player_health = player_health - 20
        # Display to the player their new stats
        print("Enemy attacks you for 20 damage!")
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
        player_health = player_health - 20
        # Display to the player their new stats
        print("Enemy attacks you for 20 damage!")
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
        player_health = player_health - 20
        # Display to the player their new stats
        print("Enemy attacks you for 20 damage!")
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