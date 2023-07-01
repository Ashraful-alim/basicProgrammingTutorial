# Problem :

# Write a Python function called "is_even" that takes an integer as input 
# and returns True if the number is even, and False otherwise.

# Solution :

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Test the function
num = 10
result = is_even(num)
print("Is the number even?", result)
