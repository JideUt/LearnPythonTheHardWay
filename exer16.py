# Exercise 16
# Learn Python the Hard way
# Reading and Writing Files
# Page 58 PDF page 74
# learning the basics of common methods and functions used with opening

# close - Closes the file, like saving
# read - reads the contents of the file and can be saved to a var
# readline - reads just one line
# truncate - empties a file
# write("string") - writes to a file, the parameter being a string

from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN or Enter.")

input("?")

print("opening the file...")
target = open(filename, 'w')

print("Truncating the file... Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")

print("Thank you. Now, I'm going to write these to the file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
target.write("\n %s \n %s \n %s \n" % (line1, line2, line3))

input("Press any key to continue...")

print("And finally, we close it.")
target.close()


print("Let's take a look")

txtfile = open(filename)
print(txtfile.read())

txtfile.close()

# With truncate() , you can declare how much of the file you 
# want to remove, based on where you're currently at in the file.
# Without parameters, truncate() acts like w, 
# whereas w always just wipes the whole file clean