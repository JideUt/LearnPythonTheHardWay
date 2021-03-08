# Exercise 15
# Learn Python the Hard way
# Reading Files
# Page 54 (PDF page 71)

# This will arguably be the most important exercise to grasp
# Reading files is the first step to interacting with data 

#imports the argumentvariable module from the sys package
from sys import argv

#unpacks argv to the script name and the filename
# remember argv allows you to take multiple arguments in commandline
script, filename = argv

#set txt variable to be the opened filename given in the argument
# open() makes a "file object"
txt = open(filename)

#prints the file name
print("Here's your file %r:" % filename)
#prints the contents of the file using the .read() function
print(txt.read())

#uses input method to prompt user to give filename
print("Type the filename again:")
file_again = input("> ")

# I BELIEVE this is the hardcoded method
txt_again = open(file_again)
print(txt_again.read())

txt_again.close()
txt.close()

