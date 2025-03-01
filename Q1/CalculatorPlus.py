import math

class Calculator:
    """
    A simple calculator class.
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

if __name__ == "__main__":
    # Create an instance of the Calculator class
    calculator = Calculator()

    # Define the numbers to be used in calculations
    num1 = 16
    num2 = 4

    # Perform and print the addition operation
    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")

    # Perform and print the subtraction operation
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")

    # Perform and print the multiplication operation
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")

    # Perform and print the division operation
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")