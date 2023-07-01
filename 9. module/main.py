# Problem :

# Create a Python program that utilizes a custom module to perform basic mathematical operations. 
# The custom module should contain functions to calculate the square and cube of a number.
# The main program should import these modules and use their functions to perform calculations based on user input.


# Solution :

from math_operations import square, cube

number = int(input("Enter a number: "))

print("Square of", number, "is", square(number))
print("Cube of", number, "is", cube(number))
