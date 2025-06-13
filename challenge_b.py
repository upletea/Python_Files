# Questions

# Uses players input to determine the output
username = input("Enter your Minecraft username: ")

# Stores wood block input that player exters as a integer
woodblocks = int(input("How many wood blocks do you have? "))

# Questions the user to input the weight of a wood block and converts it to a float
blockweight = float(input("How heavy is one of your wood blocks? (kg) "))

# Asks player if it is night or day ("must type exactly True or False")
daytime_input = input("Is it daytime in game? Type True or False: ")


if daytime_input == "True":
    daytime = True
else:
   daytime = False
# Creating a Loop
   
# Uses a while loop to inform the user if they do not posses the inventory needed and how many more they would need.
while woodblocks < 10:
    print("You have" ,woodblocks ,"wood blocks, you need", 10 - woodblocks, "more wood blocks.")
    woodblocks = woodblocks + int(input("How many more would you like to collect?"))

# Print an overall overview of the players statistics, and use multiplication (*) to get an accurate response.
print("Collection complete!")
print("Overview:")
print("Player:" , username)
print("Total Blocks:", woodblocks)
print("Total weight:" , woodblocks  *  blockweight, "kg" )

#Use if and else variable to determine if it is night or day

if daytime:
    print("It is daytime.")
else:
    print("It is nightime, watch out for mobs!")





