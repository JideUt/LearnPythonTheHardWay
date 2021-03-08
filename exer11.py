#Exercise 11
# Asking Questions
# page 42 (PDF page 59)
# This lesson is about taking input from person, changing it, and printing

print("How old are you?", end=" ")
age = input()
print("How tall are you?", end=" ")
height = input()
print("How much do you weigh?", end=" ")
weight = input()
# lesson just says to place the comma but because i'm using
# python 3 I have to do the comma and then end="" to stop it from
# going to a new line

print("So, you're %r years old, %r cm tall, and %r lbs. heavy." % (age, height, weight))

if int(weight) >= 200:
    print("wow you're heavy!")
else:
    print("thanks for playing!")