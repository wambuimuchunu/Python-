import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


    def circumference(self):
        return 2 * math.pi * self.radius

circle = Circle(7)  #radius 7
print(f"Area of the circle: {circle.area():.2f}")
print(f"Circumference of the circle: {circle.circumference():.2f}")
