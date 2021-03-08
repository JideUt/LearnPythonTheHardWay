# Exercise 30
# LPTHW
# Else and If
# Page 102 (PDF page 119)

# Exploring more features of the if-statements, including else, and eventually
	# elif.
# Again, this is not new to me but I welcome the practice and am open to
	# reviewing because perhaps there is something I missed

# if-statements create a branch in the code, like a choose your own 
    #adventure book, like zork!!
# the colon tells python that you are creating a new block of code
    # the indent of 4 spaces (or tab) tells python what lines of code
    # belong to this block

people = 30
cars = 40
buses = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")

if buses > cars:
    print ("That's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")
    
if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, let's stay home then.")

# elif stands for 'else if' which represents a different branch and circumstance
    # it means if the the first if statement does not work, try this branch with 
    # specific circumstances
    # else says, if everything proceeding does not work, do this branch of code 