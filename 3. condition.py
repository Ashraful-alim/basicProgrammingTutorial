# Problem :

# Write a Python program that takes a user's age as input and determines whether they are eligible to vote or not. 

# If the user's age is 18 or above, 
# the program should display the message "You are eligible to vote." 
# Otherwise, it should display the message "You are not eligible to vote yet."

# Solution :

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
