# Problem :
# Write a Python program that prompts the user 
# to enter a positive integer and calculates the sum of all the numbers from 1 to that integer (inclusive). 

# Display the final sum as the output.

# Solution :

num = int(input("Enter a positive integer: "))

# Initialize sum variable
total = 0

# Calculate the sum of numbers from 1 to num
for i in range(1, num + 1):
    total += i

print("The sum of numbers from 1 to", num, "is", total)
