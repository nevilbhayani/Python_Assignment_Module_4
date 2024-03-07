# Write python program that user to enter only odd numbers, else will
# raise an exception.


try: 
    num=int(input("Enter even number : "))
    if num % 2 == 0:  
        print(f"Even number is {num}") 
    else:
        print("odd number...")
except ValueError:
    print("plz enter int number...")



