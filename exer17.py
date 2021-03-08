# Exercise 17
# Learn Python the Hard Way
# More Files
# Psge 62 Page 79 of the PDF

# this lesson will copy on file to another
# important lesson to get an idea of flexibility of files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# in_file = open(from_file); indata = in_file.read()

# The below code was my original attempt to get the two lines
# above into one lines
#indata = open(from_file, 'r')
# but now I see I could just use the semicolon
# I can also do indata = open(from_file).read() and remove close at bottom
print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

#print(open(to_file, 'r'))