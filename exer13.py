#Exercise 13
#Learn Python the hard way
#Parameters, Unpacking, Variables
# Page 46 (PDF page 52)

# this lesson explains that exer13.py is an argument run in powershell
# this lesson will show how to write a script that also accepts arguments

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# the issue i was running into originally was that I didn't pass
# the three arguments into the powershell line
# in order for this to work, you have to type 
# " python exer13.py first second third " in powershell
# the arguments first second third can be anything

script, name, height, thumb = argv

oneone = input("What's your name? ")
twotwo = input("What's your height? ")
threethree = input("Which is your favourite thumb? ")

print("Welcome to the Program:", script)
print(oneone + " This is your", name)
print("You stand at about %r" % twotwo, height)
print("You said that the %r is your favourite" % threethree, thumb)
