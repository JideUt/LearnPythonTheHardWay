# Exercise 20
# Learn Python The Hard Way (LPTHW)
# Functions and Files
# Page 74 (page 91 pdf)

# straight up practice, using functions and files together

from sys import argv

script, input_file = argv

# created a function to apply read() method to a file and print it all
def print_all(f):
    print( f.read())

# I've seen seek() in the docs but never used before
# seek() brings the document back to a certain point
# in this case we set it to the sub 0 point - the beginning
# seek() method deals in bytes
def rewind(f):
    f.seek(0)
    
# probably the most interesting function
# uses the readline() method to only read a single line, separated by
# \n by default
# notice how every time the readline() method is called
# it automatically goes to the next line
# this is why it's important to use the seek() method to go back to the start

def print_a_line(line_count, f):
    print( line_count, f.readline())
    
# Here we open the file object and set it to the current_file var
current_file = open(input_file)

print("First let's print the whole file: \n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Next, let's print three lines: \n")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)