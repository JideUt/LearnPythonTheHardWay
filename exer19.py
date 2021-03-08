# Exercise 19
# Learn Python the Hard Way
# Functions and Variables
# Page 70 (PDF page 87)

# this exercise reinforces that variables inside a function are not
# connected to variables outside (global variables) of the function

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket. \nA bucket and a mop! \n")
    
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 2000)

def myfunction(number, multiple):
    value = number * multiple
    print(value)
    return value
    
myfunction(2, 5)
myfunction(amount_of_cheese, amount_of_crackers)
myfunction(myfunction(2, 8), amount_of_cheese)
