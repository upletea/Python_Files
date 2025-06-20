num1 = int(input("Enter your first number:"))  #prompts user to input their first number as an integer      
num2 = int(input("Enter your second number:"))  #prompts user to input second number as an integer
#ensure it is typed exactly (adding, subtracting) 
operation = ["adding", "subtracting"] #creates a list of operations that comes into play later on in the code
 
for i in operation:
    print(i," --") #prints the operation options for the user to choose from
operation_input = input("What operation would you like to use: adding or subtracting?")#prompts user to input if they would like to add or subtract

def calculator(operation_input, num1, num2): #makes a function and defines it
    if operation_input == "adding": # if the input is adding...
       return num1 + num2 #the number is returned as a combination of both numbers
    elif operation_input == "subtracting": #if the input is subtraction...
       return num1 - num2 #its returned as the product of that
    else:
        print("Error, operation is unsupported. No answer can be given.") #if neither adding nor subtracting is chosen, then an error message is shown
    
result = calculator(operation_input, num1, num2,) #calls the calculator function with user input and stores the result
print("Your answer is", result) #displays the final result








   
