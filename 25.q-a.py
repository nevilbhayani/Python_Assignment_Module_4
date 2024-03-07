# Explain Inheritance in Python with an example? What is init? Or What 
# Is A Constructor In Python?

# Inheritance relationship defines the classes that inherit from other classes as derived, subclass,
# or sub-type classes. Base class remains to be the source from which a subclass inherits.



# Inheritance
def demo():
    class pen:
        price=10
        color="red"
        company="cello"


        def show(self):
            print(f"price: {self.price} , color : {self.color} , company :{self.company}")

    class notebook(pen):
        def __init__(self):
            pass

        def ok(self):
            print(f"price: {self.price} , color : {self.color} , company :{self.company}")

    s=pen()
    s.show() 
    s1=notebook()
    s1.ok()

demo()



# What is init? Or What 
#  __init__ method is like default constructor in C++ and Java. Constructors are used to initialize the object's state. The task of constructors is to
# initialize(assign values) to the data members of the class when an object of the class is created.


# Is A Constructor In Python?
# ---> A constructor is a special method in a class used to create and initialize an object of a class.
#      There are different types of constructors in Python programming language. Constructor is invoked automatically
#      when an object of a class is created