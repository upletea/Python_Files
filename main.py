# Practical 1
# Making a simple output statement

print("Bloom Baby Bloom")

score = 100

lives = 0    

print()

print("Your score is:", score)

# print(score)

# Sequence (do this, then that) - 1

print("Hello")

print("Welcome to the program")

# Selection (decision making) - 2
if score >= 50:
    print("You passed!")

else:
    print("Try again.")

# Iteration (Loops) - 3

# use loops to repeat actions
   
    # while loop (repeats until a condition is false)
while lives > 0:
    print("Keep playing")
    
    # for loop (repeats over a list or range)
for level in range(1, 4): #type : ignore
    print("Level", level)

# Variable and Data Types - 4

# Variables store information. Data types include:
  # int - numbers (e.g. 5)            
  # str - text (e.g. "hello"
  # bool - true or false
  # list - collection of the items (e.g. (1.2.3))     

name = "Aapti"
score = 10
passed = True  

#Functions (Reusable blocks) - 5

#functions let you organize code and reuse it.

def greet(name):
    print("Hello", name)

greet("Uptea")

#Input and Output - 6

name = input("Enter your name: ")
print("Hi", name)
# Practical 2


