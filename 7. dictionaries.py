# Problem :
# Create a Python program that stores information about a person in a dictionary. 
# The dictionary should include the person's name, age, and favorite color. 
# The program should prompt the user to enter these details, store them in the dictionary, and then display the dictionary's contents.

# Solution :

person = {}

person['name'] = input("Enter the person's name: ")
person['age'] = int(input("Enter the person's age: "))
person['favorite_color'] = input("Enter the person's favorite color: ")

print("Person's Details:")
for key, value in person.items():
    print(key.capitalize() + ':', value)
