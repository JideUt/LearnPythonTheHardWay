# Exercise 10
# What was that?
# Page 38 (Pdf page 55)
# the backslash is an escape sequence
# \\ adds a single backslash, \" escapes the double quote inside the string

tabby_cat = "\tI'm tabbed in." # I never knew \t about the tab before now
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# I like the use of the * after \t to create bullets
print( tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# while True:
#    for i in ["/", "-", "|", "\\", "I"]:
#        print("%s\r" % i)

dogname = "Ralph"

introductioncall = "Hi you. Have you met my dog, %s? %s\'s such a good boy"

print(introductioncall %(dogname, dogname))
