# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function and print the result
result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")

# Contributor @parikshith078
def funbonci(n):
    if n <= 0:
        return "Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    
    return b
