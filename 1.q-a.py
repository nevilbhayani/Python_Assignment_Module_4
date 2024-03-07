# What is File function in python? What is keywords to create and write file.

# The key function for working with files in Python is the open() function. The open() function takes two parameters; filename, and
# mode. There are four different methods (modes) for opening a file: "r" - Read - Default value. Opens a file for reading, error if the
#  file does not exist.

f = open("q-1.txt",'w')
f.write("hello.\n")
f.write("i am a full stack developer.\n")
f.write("my name is nevil bhayani.")
