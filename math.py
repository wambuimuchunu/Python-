import math
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: ")) 

# Calculate the surface area using the formula: SA = 2πr² + 2πrh
surface_area = 2 * math.pi * radius ** 2 + 2 * math.pi * radius * height

print(f"The surface area of the cylinder is: {surface_area:.2f} square units.")
