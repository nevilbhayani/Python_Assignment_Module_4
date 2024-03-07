#  Write a Python program to count the number of lines in a text file.

file=open("q-9.txt","r")  
count=0 
for i in file: 
    if i[0] not in "":  
        count+=1 
print(count) 
        
file.close()