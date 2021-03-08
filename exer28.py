# Exercise 28
# LPTHW
# Boolean Practice
# Page 96 (PDF page 113)

# Practicing the Boolenan logic expressions that I am very familiar with
# Although I am familiar, I will not be skipping any practice for concepts

# The following are the questions and my answers below:
True and True == True #correct
False and True == False
1 == 1 and 2 == 1 == False
"test" == "test" == True
1 == 1 or 2 != 1 == True
True and 1 == 1 == True
False and 0 != 0 == False
True or 1 == 1 == True
"test" == "testing" == False
1 != 0 and 2 == 1 == False
"test" != "testing" == True
"test" == 1 == False
not (True and False) == True
not (1 == 1 and 0 != 1) == False
not (10 == 1 or 1000 == 1000) == False
not (1 != 10 or 3 == 4) == False # WRONG !!! Inside brackets False, not flips!
not ("testing" == "testing" and "Zed" == "Cool Guy") == True
1 == 1 and not ("testing" == 1 or 1 == 0) == True
"chunky" == "bacon" and not (3 == 4 or 3 == 3) == False
3 == 3 and not ("testing" == "testing" or "Python" == "Fun") == False

print(True and True)
print(False and True)
print(1 == 1 and 2 == 1)
print("test" == "test")
print(1 == 1 or 2 != 1)

print(True and 1 == 1)
print(False and 0 != 0)
print(True or 1 == 1)
print("test" == "testing")
print(1 != 0 and 2 == 1)

print("test" != "testing")
print("test" == 1)
print(not (True and False))
print(not (1 == 1 and 0 != 1))
print(not (10 == 1 or 1000 == 1000))

print(not (1 != 10 or 3 == 4) == False)
print(not ("testing" == "testing" and "Zed" == "Cool Guy"))
print(1 == 1 and not ("testing" == 1 or 1 == 0))
print("chunky" == "bacon" and not (3 == 4 or 3 == 3))
print(3 == 3 and not ("testing" == "testing" or "Python" == "Fun"))

# Got 19 out of 20 correct, missed one by not identifying 1!=10 as True
# Simple oversight