# Exercise 21
# LPTHW
# Functions Can Return Something
# Page 78 (PDF page 95)

# Learning about the use-case for the return function
# return sets variables up to be a value from a function

def add(a, b):
    print("Adding %d + %d" % (a, b))
    return a+b
    
def subtract(a, b):
    print("Subtracting %d - %d" % (a, b))
    return a - b
    
def multiply(a, b):
    print("Multiplying %d * %d" % (a, b))
    return a * b
    
def divide(a, b):
    print("Dividing %d / %d" % (a, b))
    return a / b 

print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age,height, weight, iq))

# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

# Python adds the two numbers in the function. When the function ends,
# the return saves the value which can now be assigned to a variable 
# I need to take extra care to differentiate between print (a None function)
# and return (adds value to the function object) and can be assigned
# to a variable

