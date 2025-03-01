import math

class GeometryCalculator:
    """
    A class for calculating geometric areas.
    """

    def calculate_circle_area(self, radius):
        """
        Calculates the area of a circle.

        Args:
            radius: The radius of the circle (a numerical value).

        Returns:
            The area of the circle (a numerical value).
        """
        return math.pi * radius ** 2  # Area = pi * radius squared
    
    def calculate_rectangle_area(self, length, width):
        return length * width


if __name__ == "__main__":
    # Create an instance of the GeometryCalculator class
    calculator = GeometryCalculator()

    # Define the radius of the circle
    radius = 5

    # Calculate and print the area of the circle
    print(f"The area of the circle with radius {radius} = {calculator.calculate_circle_area(radius)}")

    # Feature: Calculate area of a rectangle
    length = 10
    width = 6
    print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width)}")
