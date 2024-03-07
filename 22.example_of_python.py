# How to Define a Class in Python? What Is Self? Give An Example Of 
# A Python Class


 # A class in Python can be defined using the class keyword. As per the syntax above,
#       a class is defined using the class keyword followed by the class name and : operator after the class name,
#       which allows you to continue in the next indented line to define class members.
    



class MyClass:
    def __init__(self, name):
            self.name = name

    def demo(self):
            print("python," + self.name)

p1 = MyClass("java")
p1.demo()

