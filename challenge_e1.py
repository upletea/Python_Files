num1 = int(input("Enter your first number:"))  #user inputs their first number as an integer      
num2 = int(input("Enter your second number:"))  #user inputs second number as an integer
#ensure it is typed exactly (adding, subtracting) 
operation = ["adding", "subtracting"] #creates a list of operations that comes into play later on in the code
 
for i in operation:
    print(i," --") #prints the operation options for the user to choose from
operation_input = input("What operation would you like to use: adding or subtracting?")#prompts user to input if they would like to add or subtract

def calculator(operation_input, num1, num2): #creates a function 
    if operation_input == "adding":
       return num1 + num2
    elif operation_input == "subtracting":
       return num1 - num2
    else:
        print("Error, operation is unsupported. No answer can be given.")
    
result = calculator(operation_input, num1, num2,)
print("Your answer is", result)




   
