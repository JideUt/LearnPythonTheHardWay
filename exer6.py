# Exercise 6
# Strings and Text
# Learning what strings do

#setting the variables x, binary, do_not, and y
#using format characters in x and y to practice 
#including information outside of the string
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

# using the format character r, which stands for repr()
# repr() uses the printable version of the variable
# format character s, stands for str()
print("I said: %r." % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

# concatenation of strings
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

