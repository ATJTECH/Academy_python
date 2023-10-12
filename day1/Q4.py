class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error! Division by zero."
        return x / y

# Example usage of the Calculator class
calc = Calculator()
num1=int(input("Enter a number"))
num2=int(input("Enter another number"))
print("Addition:", calc.add(num1,num2))
print("Subtraction:", calc.subtract(num1,num2))
print("Multiplication:", calc.multiply(num1,num2))
print("Division:", calc.divide(num1,num2))