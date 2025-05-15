"""
A class for representing a circle
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def display_circumference(self):
        print(f"circumference: {2 * 3.14 * self.radius} units")

    def display_area(self):
        print(f"area is: {3.14 * self.radius ** 2} square units.")


circle1 = Circle(3)
print(f"radius: {circle1.radius} units")
circle1.display_circumference()
circle1.display_area()
