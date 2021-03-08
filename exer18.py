#Exercise 18
# Learn Python the Hard Way
#Names, Variables, Code, Functions
# Page 66, Page 83 in PDF

#function introduction
# Functions do 3 things
# They name a piece of code the way variables name strings and numbers
# they take arguments the way scripts take argv
#they combine those 2 things to make mini scripts and tiny commands

# this is an example of creating a func similar to argv
# uses the unpacking method with the asterisk
# * tells python to take all arguments and put them in argument as a list
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" %(arg1, arg2))
    
# this just takes one argument
def print_one(arg):
    print("arg1: %r" % arg)

# this one takes no arguments
def print_none():
    print("No Arguments Here")

print_two("Jide", "Utomi")
print_two_again("Jide", "Wincy")
print_one("one argument")
print_none()

