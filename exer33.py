# Exercise 33
# LPTHW
# While-Loops
# Page 110 (PDF page 127)

# This lesson needs tremendous focus. While-Loops are a weak spot for me
	# in terms of how to best use this tool
# The while loop will continue executing until the Boolean Expression is changed.
# Make sure that while loops are used sparingly
# Make sure that the thing you are testing will become False at some point
# When in doubt print it out



def listing_numbers(num, inc):
    i = 0 
    numbers = []

    while i < num:
        print("At the top i is %d" % i)
        numbers.append(i)
    
        i += inc
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print ("The numbers: ")

    for num in numbers:
        print (num)
        

def forlooplisting(start, fin, inc):
    
    newlist = []
    
    for i in range(start, fin, inc):
        if len(newlist) == 0:
            print("We start with an Empty List")
        else:
            print("\nBefore the loop, the last number is %d" % newlist[len(newlist)-1])
        newlist.append(i)
        print("\n\t", newlist)
        print("\nAfter the loop, the last number is now %d " % newlist[len(newlist)-1])
        


beginning = int(input("Choose a number to start the list: "))
lastnumber = int(input("Choose a number to end the list: "))
increment = int(input("Choose an increment to go by: "))
forlooplisting(beginning, lastnumber, increment)
listing_numbers(lastnumber, increment)