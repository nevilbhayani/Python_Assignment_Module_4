# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        return area


l_input = float(input("Enter the length : "))
w_input  = float(input("Enter the width  : "))


demo = Rectangle(l_input, w_input)  
area = demo.calculate_area()
print(f"The area of the rectangle is : {area}")
