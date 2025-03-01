import math

class Calculator:
    """
    A simple calculator class with basic arithmetic operations and square root.
    """

    def add(self, a, b):
        """
        Adds two numbers.
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtracts b from a.
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiplies two numbers.
        """
        return a * b

    def divide(self, a, b):
        """
        Divides a by b.
        """
        return a / b

    def square_root(self, x):
        """
        Calculates the square root of x.
        """
        return math.sqrt(x)

if __name__ == "__main__":
    # Create an instance of the Calculator class
    calculator = Calculator()

    # Define the numbers for basic arithmetic calculations
    num1 = 16
    num2 = 4

    # Perform and print addition
    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")

    # Perform and print subtraction
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")

    # Perform and print multiplication
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")

    # Perform and print division
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

    # Define a number for square root calculation
    num3 = 25

    # Perform and print the square root calculation
    print(f"The square root of {num3} = {calculator.square_root(num3)}")