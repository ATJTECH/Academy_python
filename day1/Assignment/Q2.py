def multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")

# Get user input for the number
try:
    number = int(input("Enter a number: "))
    multiplication_table(number)
except ValueError:
    print("Invalid input. Please enter a valid number.")