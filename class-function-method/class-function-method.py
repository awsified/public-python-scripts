# This should thoroughly give an example of how functions, classes, and methods interact within Python.

# function
def double(x):
    return x * 2

# class
class MyClass(object):
    # method
    def myMethod(self): # self references the attributes and methods within the class.
        print ("Hello, World")

myObject = MyClass()
myObject.myMethod()  # will print "Hello, World"

print(double(5))  # will print 10