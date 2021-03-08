# Exercise 31
# LPTHW
# Making Decisions
# Page 104 (PDF page 121)

# the power of if, elif and else is to give your script the ability to
	# make decisions!!!!

print("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    
    bear = input("> ")
    
    if bear == "1":
        print("The bear eats your face off. Good job!")
        print("You run around in a panic while the bear enjoys chewing on your face.")
        print("1. You run towards the bear gnawing sound.")
        print("2. You run away from the bear chewing sound.")
        
        run_away = input("> ")
        
        if run_away == "1":
            print ("The bear grants you a quick death. Great Job!")
        elif run_away == "2":
            print("You run into a wall and the bear laughs at you!")
        else:
            print("Your indecision makes the bear confused. He runs away.")
    
    elif bear == "2":
        print("The bear eats your leg off. Good job!")
        print("1. You grab your loose leg and hit the bear over the head.")
        print("2. You hop away from the bear busily chewing your old leg.")
        
        got_your_leg = input("> ")
        
        if got_your_leg == "1":
            print ("The bear takes the leg and slaps you back! Hahaha!")
        elif got_your_leg == "2":
            print("You run into a wall and the bear laughs at you!")
        else:
            print("Your indecision makes the bear confused. He runs away.")
    
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's anus.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling the lyrics to 'Moon River'")
    
    insanity = input("> ")
    
    if insanity == "1" or "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Yikes!")
else:
    print("You stumble around and fall on a knife and die. Probably the best way to go!")
    
    