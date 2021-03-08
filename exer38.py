# Exercise 37
# LPTHW
# Doing Things to Lists
# Page 128 (PDF page 145)

# Back to learning about the different functions that can act on Lists
# the append function has two parameters as shown in the example

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There's %d items now." % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # Negative indexing
print(stuff.pop())
print(' '.join(stuff)) # This will be a useful method along with .pop()
print('#'.join(stuff[3:5]))

# Part of the study drills is to read about OOP
# I have watched several videos but I don't know that I'm any more familiar with
# it than before

#OOP 4 pillars
    #Encapsulation - group related func and vars together to reduce complexity
        # and increase reusability
    #Abstraction - Hide the details and complexity to isolate the impact of
        #changes
    #Inheritance - Eliminate redundant code
    #Polymorphism - refactor ugly switch case statements

# The next study drill says to look up Classes
