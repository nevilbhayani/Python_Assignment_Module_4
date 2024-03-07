#Write a Python program to read a file line by line store it into a variable.


f = open("q-1.txt", "r")

lines = f.readlines()

for line in lines:
    words = line.split()
    print(line)

f.close() 
