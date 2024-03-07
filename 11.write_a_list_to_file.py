# • Write a Python program to write a list to a file.

items = ['nevil ', 'meet ', 'om ', 'raj ', 'krish ']
file = open('q-11.txt','w')
file.writelines(items)
file.close()
