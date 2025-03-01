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

if __name__ == "__main__":
    # Create an instance of the GeometryCalculator class
    calculator = GeometryCalculator()

    # Define the radius of the circle
    radius = 5

    # Calculate and print the area of the circle
    print(f"The area of the circle with radius {radius} = {calculator.calculate_circle_area(radius)}")