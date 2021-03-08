# Exercise 32
# LPTHW
# Loops and Lists
# Page 106 (PDF page 123)

# Loops and Lists - both very powerful tools 
# For and while loops are commonly used in programs and add to the decision trees
# Lists are powerful and can be indexed through: A container of things.

the_count =  [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print("This is count %d" % number)

for fruit in fruits:
    print("A fruit of type: %s" % fruit)

#we can iterate through mixed lists with both integer and strings
# perfect time to use %r 

for i in change:
    print("I got %r" % i )

# we can build lists by starting with empty one assigned to variable

elements = []

# then use the range built-in function to do 0 to 5 counts
for i in range(0,6):
    print("Adding %d to the list." % i)
    # append is a function that is used on lists
    elements.append(i)
    
#now we can print them out too
for i in elements:
    print("Element was: %d" % i)

print(elements)

#newlist = [*range(10,21)]
#print(newlist)



