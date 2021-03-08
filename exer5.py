# Exercise 5 of Python the hard way
# trying to get me used to variables and format strings

my_name = "Jide Wincy Utomi"
my_age = 31
my_height = 183 #centimeters
my_weight = 202 # pounds
my_eyes = "Brown"
my_teeth = "whiteish"
my_hair = "black"

# I had issues making the following run because I put the % and variable outside of the parentheses 
print("Let's talk about %s " % my_name )
print("He's %d centimeters tall." % my_height )
print("He's %d pounds heavy." % my_weight )
print("Actually, that's obese according to the BMI")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on if he brushed that day" % my_teeth)

# this line shows you can uyse multiple format strings in a single string

print("If I add %d, %d, and %d, I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

