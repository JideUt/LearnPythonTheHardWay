# Exercise 14
# Learn Python the Hard Way
# Prompting and Passing
# Page 50 (PDF Page 67)

# the author stated using argv and input() will be very important
# to reading files in the next lesson


from sys import argv

script, user_name = argv
prompt = 'Type Here: ' # This never came to my mind to do
# setting the input prompt under a variable allows me to change it
# in one spot later on! Smarrrttttt


print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)

likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice stuff!
""" %(likes, lives, computer))
 
