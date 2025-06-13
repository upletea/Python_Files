#EXERCISE 1

# Ask for the user's name
name = input("Enter your name: ")

# Ask for the user's age and convert to integer
age = int(input("How old are you? "))

# Ask for favourite snack
snack = input("What is your favourite snack? ")
 
# Ask how long they want to play and convert to float
minutes = float(input("How long do you want to play for? "))

# Ask if they like water play (must type True or False exactly)
waterplay_input = input("Do you like water play? Type True or False: ")

# Convert string input directly to boolean (only works if exactly 'True' or 'False')
if waterplay_input == "True":
    waterplay = True
else:
   waterplay = False

# Print a message based on their waterplay preference
print("new waterplay is", int(waterplay))  # True becomes 1, False becomes 0

# Final personalised message
print("You are", age, "years old and ready to play with Bluey in the backyard.")
print("You will play for", minutes, "minutes and bring your favourite snack:", snack + ".")

# Print a follow-up message about waterplay

if waterplay:
    print("You will do waterplay, better bring a towel!")
else:
    print("You will skip waterplay but still enjoy yourself!")

# EXERCISE 2

games_list = ["Keepy Uppy", "Magic Asparagus", "Shadowlands", "Obstacle Course", "Muffin Cone"]
print(games_list)

print("First game:", games_list[0])
print("Last game:", games_list[-1])

games_list.append("Grannies")
print(games_list)

games_list[1] = "Magic Wand"
print(games_list)

for game in games_list:
    print("Let’s play:", game)

def count_games():print("Total games:", len(games_list))

count_games()