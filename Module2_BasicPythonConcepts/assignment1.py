""" 
Task 1: Perform Basic Mathematical Operations Problem Statement: 
Write a Python program that does the following: 
1. Takes two numbers as input from the user. 
2. Performs the basic mathematical operations on these two numbers:
o Addition 
o Subtraction 
o Multiplication 
o Division 
3. Displays the results of each operation on the screen.

"""
# Task 1: Perform Basic Mathematical Operations

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# To avoid division by zero. 
if num2 != 0:
    division = num1 / num2
else:
    division = "(Cannot divide by zero)"

print("\n------ Results ------")
print(f"Addition:  {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")



#Task 2 : Create a Personalized Greeting. 

first_name = input("\nPlease enter your first name: ")
last_name = input("Please enter your last name: ")

# Combine first and last name
name = first_name + " " + last_name

# Display personalized greeting as output. 
print("Hello, " + name + "! Welcome to the Python program.")


