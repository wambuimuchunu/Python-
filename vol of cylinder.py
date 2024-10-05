import math
def cylinder_volume(radius, height):
    
    volume = math.pi * radius * radius * height
    return volume


r = float(input("Enter the radius of the cylinder: "))
h = float(input("Enter the height of the cylinder: "))


print("The volume of the cylinder is:", cylinder_volume(r, h))

