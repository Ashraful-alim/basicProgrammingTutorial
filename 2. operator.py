# Problem :
# Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

# Solution :

pi = 3.1416

radius = float(input("Enter the radius of the circle: "))

area = pi * radius ** 2

print("r =", radius)
print("Area =", area)
