# • Write a Python program to read a file line by line and store it into a list


with open('q-1.txt', 'r') as file:
    lines = file.readlines()
print(lines) 