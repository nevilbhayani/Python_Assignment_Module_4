# • Write a python program to find the longest words


f = open("q-1.txt",'r')
text = f.read()
print(text)


n=int(input("Enter A number : "))
list1=[] 
for i in range(n):  
    str1=input("Enter  string: ")
    list1.append(str1) 
    s=sorted(list1,key=len) 
print(s[-1])
    
jhbjv