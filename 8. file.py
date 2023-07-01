# Problem :

# Create a Python program that reads the contents of a text file and counts the number of lines, words, and characters in the file. 
# The program should then display these counts to the user.

# Solution :

file_path = input("Enter the path to the text file: ")

lines = 0
words = 0
characters = 0

with open(file_path, 'r') as file:
    for line in file:
        lines += 1
        words_list = line.split()
        words += len(words_list)
        characters += len(line)

print("Number of lines:", lines)
print("Number of words:", words)
print("Number of characters:", characters)
