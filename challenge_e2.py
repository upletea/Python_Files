num1 = int(input("Enter your first number:"))  #user inputs their first number as an integer      
num2 = int(input("Enter your second number:"))  #user inputs second number as an integer

def compare_numbers(num1, num2): #defines the function that compares the two inputted numbers
    if num1 > num2: #if the first number inputted is larger...
       return num1 #the program returns num1 variable
    elif num1 < num2: #if the second number inputted is larger...
        return num2 #the program returns num2 variable
    else: #However, if the numbers are equal to one another...
        print("The numbers are equal to one another!") #a message is printed that says that the numbers are equal to one another

result = compare_numbers(num1, num2) #This shows the result of the function compare_numbers 

if result == num1: #If the result is num1...
    print("The first number is greater!") #This message is outputted
elif result == num2: #If the result is num2...
    print("The second number is greater!") #This message is outputted





