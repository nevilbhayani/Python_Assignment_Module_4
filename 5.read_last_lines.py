# Write a Python program to read last n lines of a file.

f = open("q-1.txt","r")
# data=f.read()
# print(data)

# line1=f.readline()
# print(line1)

# line2=f.readline()
# print(line2)

# line3=f.readline()
# print(line3)

# line4=f.readline()
# print(line4)

with open ("q-1.txt","r") as f:
    for line in f:
        pass
    last_line=line
print(last_line)


f.close()
