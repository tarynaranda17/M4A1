# Calculator Program
# M4Lab1ii.py for M4 Assignment 1
# C. Calongne, 01/19/19

# Seven steps to complete in this lab: 
# Define a list to store the choices for +, -, *, /
# Define 3 functions with local variables
# Define three elif statements that call the functions for -, *, and /

# Local variables are visible in the functions
# Pass the input values into them.
# Continue calculating until the user presses "n"

print("Welcome to your Calculator program")

# The add function adds two numbers 
def add(x, y):
   return x + y
   # local scope; only the add() function sees x and y

#write the other three functions for subtract, multiply and divide

# Step 1: Write a subtract function that subtracts two numbers 

def subtract(x,y):
    if x==int(x) or float(x) and y==int(y) or float(y):
       result= x-y
# Step 2: Write a multiply function that multiplies two numbers
def multiply(x,y):
   if x== float(x) or int(x) and y== float(y) or int(y):
      your_result= x*y

# Step 3: Write a divide function that divides two numbers
def divide(x,y):
 if x==float(x) or int(x) and y==float(y) or int(y):

# Start calculating 
# Step 4: define a list called choice with + - * / in it

keep_going ==["y", "n"]:
   
while keep_going != "n"

    num1 = float(input("Enter first number: "))
    choice = input("What kind of calculation? Choose one of: +, -, *, /  ")
    num2 = float(input("Enter second number: "))

    if choice == "+":
        # choice is a list with the string value for "+"
        # The test for choice returns the value True or False. If true:

        print(num1, choice, num2,"+", add(num1,num2))
        # calls the add function and passing it two parameters

    # finish the rest of the if statement for the other 3 calculations
                           
    # Step 5: write an elif for subtract
    if choice=="-":
       print(num1, choice, num2,"-", add(num1,num2))

    # Step 6: write an elif for multiply
    if choice=="*":
       print(num1, choice, num2,"*", add(num1,num2))

    # Step 7: write an elif for divide
    if choice=="/":
       print(num1, choice, num2,"/", add(num1,num2))
    
    
    else:
        print("Invalid input")

    keep_going = input("Calculate? y or n? ")    
print("Closing the calculator.")
