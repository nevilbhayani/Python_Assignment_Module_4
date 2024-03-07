#  How Do You Handle Exceptions With Try/Except/Finally In Python? 
# Explain with coding snippets

try: 
    a=int(input("Enter A number : "))
    print(a)
except ValueError: 
    print("plz type a int....")
finally:
    print("thank you...")

