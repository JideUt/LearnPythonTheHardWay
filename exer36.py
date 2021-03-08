# Exercise 36
# LPTHW
# Designing and Debugging
# Page 120 (PDF page 137)

# I can honestly say I don't know much about debugging, so this will
	# be quite an important chaprter to come back to

# Rules for If-Statements (For better code!)
	# 1. Every If Statement must have an else
	# 2. If the else is based on something that should never happen,
		# you use a die function that prints an error message and ends
		# the script. This will reveal many errors
	# 3. Try to not nest if statements more than 2 deep. If at all possible,
		# try to make it only 1 deep.
	# 4. Treat if statements like paragraphs, where each if, elif and else
		# is grouped on its own lines with spaces between
	# 5. Boolean tests should be simple, and if they are complex, move their
		# calculation to a variable with a good name.

	# 6 (Bonus). Rules are made to strengthen your design and mind. But in real
		# life, sometimes the rules are stupid and can get in the way of function

# Rules for Loops (For better code!)
	# 1. Use while-loop only to loop forever, which means very seldom
	# 2. Use for-loop for all other kinds of looping, especially if there
		# is fixed or limited number of things to loop over

#Tips for Debugging
	# 1. Do not use a "debugger." A debugger is like doing a full-body scan
		# on a sick person. You don't get specific enough information.
	# 2. The best way to debug is to use print to print out the values of
		# variables at points in the program to see where it goes wrong
	# 3. Make sure parts of your program work as you work on them. Do NOT
		# right massive scripts without testing a bit at a time. Code a little,
		# run a little, fix a little.


# Create your own text adventure game like exercise 35
# map out the game first before writing code
import time
from sys import exit


def mainroom(name):
    print("\n\t------------------------------------------")
    print("\t You have entered The Hall of Judgement")
    print("\t------------------------------------------")
    time.sleep(2)
    print("\nMysterious Voice: Look, I didn't name the rooms, I'm just The \
Custodian! But Trust me, it's much scarier than it sounds!")
    print("""\n(Custodian):In front of you lies three doors:
    \t* The Red Door
    \t* The Blue Door
    \t* The Orange Door
\nYou must choose a door and your only mission is to survive!
    """)
    time.sleep(2)
    print("So choose a door and seal your fate!")
    print("""\n\t**Hint: Try typing 'look around'**\n""")

    prompt = input("> ").lower()


    if prompt == 'red' or prompt == 'red door' or prompt == '1':
        print("You have chosen the Red Door")
        print("""\t%s, on the other side of that door is a
Lake of Fire!!! As soon as you opened the door, it disappeared
and the main room vanished. All that there is now is wall behind you,
the small ledge that you're standing on, and in the middle of the lake
is a cup on a platform. It's starting to get really hot!""" % name)
        time.sleep(2)
        reddoor(name)
    elif prompt == 'blue' or prompt == 'blue door':
        print("You have chosen the Blue Door")
        print("""\t%s, You've been transported to a frozen mountain top!
The door has vanished behind you and there is nothing but snow everywhere...
It doesn't seem like you were dressed for a frozen tundra.""" % name)
        time.sleep(2)
        bluedoor(name)
    elif prompt == 'orange' or prompt == 'orange door':
        print("You have chosen the Orange Door")
        print("""\t%s, You've walked out of a tree and you are surrounded by
the tallest forest you have ever seen! When you look behind you, the tree you just \
walked out of is completely solid. You think it's day time but the canopy above you \
completely blocks out the sky. It's eerily quiet, with only the subtle sound of the \
breeze rustling against the leaves above and the crunch of dead leaves beneath \
your feet.""" % name)
        time.sleep(2)
        orangedoor(name)
    elif prompt == 'look around' or prompt == 'look':
        print("You look closer at your surroundings")
        print("""\n\t You notice the red door has a brass handle. It almost looks\
red itself. Like a hot iron. Maybe it's just the reflection of the door itself\n
""")
        time.sleep(2)
        print("""\n\t The Blue door seems to be frosted. The door knob looks like\
a block of ice! This door is larger than the red door and orange door combined!\n
""")
        time.sleep(2)
        print("""\n\t The Orange door is wooden and appears brown at first glance.\
Instead of a door knob, there's a handle. And this is the smallest of the doors.\
You notice the corners of this door are rounder than the others.\n
""")
        time.sleep(2)
        print("\t **********************************************")
        time.sleep(2)
        print("""\n\t When you try to turn around to look at the rest of the
Hall of Judgement, the doors shift to be right in front of you!! Above and below\
you is nothing but blackness!\n
""")
        time.sleep(2)
        mainroom(name)
    else:
        print("\nThe Custodian: You had so much to choose from, %s... and yet you decided to choose\
		something else")
        print("**Your Blood stops pumping, You die slowly**")
        exit(0)

def reddoor(name):
    print("\n\t------------------------------------------")
    print("\t            The Lake of Lava!")
    print("\t------------------------------------------")

    print("\n%s, what are you going to do?\n" % name)
    print("""You have two clear choices:
    *1. Look around for something to help
    *2. It's probably an illusion so just walk across the lake of lava""")

    nextmove = input("So will it be choice 1 or 2? ")

    if nextmove == "1":
        time.sleep(1)
        print(""" \t\n Well well well, aren't we smart!
You found a red ladder that blended in to its surroundings! It looks like the \
perfect length to reach the pedastle in the middle of this lava lake. Now the only \
Question is whether you are brave enough to walk across?""")
        lavatime(name)
    else:
        time.sleep(1)
        print("""\tAre you an idiot? It's REAL! You fall into it immediately beginning
to burn to death. Bye Felicia!""")
        exit(0)

def bluedoor(name):
    print("\n\t------------------------------------------")
    print("\t           The Frozen Mountain Top!")
    print("\t------------------------------------------")
    print("\n%s, what are you going to do?\n" % name)
    time.sleep(2)
    print("The Snowy Tundra is blinding and is chilling to the bone!")
    time.sleep(2)
    print("\nCustodian: This is the hardest challenge available! %s, Your soul\
must've brought you here because you can handle it!" % name)
    time.sleep(2)
    print("\nYou can barely see your hands in front of you, but where you appeared\
there's a frozen man decked out in winter gear and climbing gear.")
    time.sleep(2)
    print("So what are you going to do? Your options:")
    print("""\n\t 1. You can take the gear off of the corpse... it's kinda gross!
\n\t 2. You can stay here and wait for help.
\n\t 3. You can try walking down the mountain without taking the dead guy's stuff!""")

    icechoice = input("\n Make your choice! 1, 2, or 3: ")

    if icechoice == "1":
        time.sleep(2)
        print("\nCustodian: Obviously this was the right choice!")
        time.sleep(1)
        print("\nYou reach down to strip the corpse and notice is eyes were frozen\
open! You rip the clothing off and its very difficult, everything is as stiff as a\
board")
        time.sleep(2)
        print("As you make your way down the mountain, you notice the feeling of\
snow crunching beneath your feet is slowly becoming less and less")
        time.sleep(2)
        print("\n The White-out becomes a Grey-out...")
        time.sleep(1)
        print("\n... And then Black-Out")
        victorious(name)
    elif icechoice == "2":
        time.sleep(2)
        print("\nYeah, if you wait here, something will just magically happen")
        time.sleep(2)
        print("\n...")
        time.sleep(2)
        print("\n\t... 2 Hours Later ... ")
        time.sleep(1)
        print("\nCustodian: Oh you're still sitting there %s?" % name)
        print("\n You're shivering uncontrollably, your lips are blue and you\
can't feel anything in your body")
        time.sleep(1)
        print("\nCustodian: So, your choice was pretty dumb! I'm just going to let\
you suffer the consequences of your decisions. Have a good death!")
        time.sleep(1)
        print("\n...")
        time.sleep(5)
        print("\nFinally, you die... and lose!")
        print("\n ")
        exit(0)

    else:
        print("\nCustodian: *Heavy Sigh* Look, I'm not going to let you play anymore\
if these are the kind of decisions you're going to make. *Loud Snap*\n")
        time.sleep(1)
        print("You Collapse in the snow, face first")
        time.sleep(2)
        print("\nCustodian: Take a moment and think about how your life ends here")
        time.sleep(2)
        print("\nYou feel the flame of life extinguish... And you die...")
        print("\n ")
        exit(0)
def orangedoor(name):
    print("\n\t------------------------------------------")
    print("\t             The Dark Forest!")
    print("\t------------------------------------------")

    print("\n%s, what are you going to do?\n" % name)
    print(""" You have two choices:
\t*1. You can walk deeper into the forest to inspect your surroundings.\n
\t*2. You can stay where you are and cry for help.
    """)

    nextmove = input("So what will you do? 1 or 2? > ")

    if nextmove == "1":
        time.sleep(1)
        print(""" \t\n Bold Move!
You stumble your way into the dark and in your first couple of steps you kick \
something with your foot. You rustle through the noisey leaves to grab it. You\
find a lighter. It gives you a sense of relief and you pocket the lighter.
        """)
        print("\t\t\n OBTAINED: LIGHTER\n")
        ogre(name, 1)
    else:
        time.sleep(1)
        print("""You decided you cannot take this anymore and Yell at the top of
your lungs! Screaming for anyone to help you!""")
        ogre(name, 0)

def ogre(name, lighter):

    time.sleep(2)
    print("\n Your noiseiness woke something up! A monstrous yell can be heard\
and felt vibrating through every bone in your body! It's very close by")

    if lighter == 1:
        time.sleep(2)
        print("You take the lighter out of your pocket to illuminate the darkness.\
For that brief second, you really wish you hadn't... There's an Ogre staring\
back at you!")
    else:
        print("You put your hands out in front of you to feel in the darkness.\
         You feel what seems to be a warm rock covered in moss...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(2)
        print("\n Your skin begins to crawl as you realize the slimey rock feels\
         like it's breathing. As your eyes begin to adjust to the dark its too late.")
        print("\n You look up to see a mouth coming over your head. %s, that's the\
        last thing you'll ever see... You've been eaten by an Ogre" % name)
        exit(0)
    print("You have to fight! Will you:\n")
    print("\t 1. Charge the ogre? Kicking and Screaming!\n\t 2. Use the lighter\
to light the dry leaves")

    time.sleep(1)
    finalchoice = input("1 or 2")

    if finalchoice == "1":
        print("Well at least you're brave... And you died that way! Rest in Power\
 %s" % name)
    elif finalchoice == "2":
        print("Wisdom will defeat all those who stand in your way!")
        time.sleep(1)
        print("Ogre: ARRRAGGHHHHHH!!!!!")
        time.sleep(1)
        print("The Ogre cannot take the heat and runs away")
        victorious(name)
    else:
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("Custodian: So... I give you the answer and you choose to do\
nonsense instead? *Custodian snaps his fingers*")
        time.sleep(2)
        print("You feel an immense tension in your skin... The custodian is tearing\
you apart by your molecules... You can tell he is killing you in the worst way!")
        time.sleep(1)
        print("You're dead")

def lavatime(name):
    time.sleep(1)
    print("""You're able to successfully put the ladder in place. But what is the
best way to get across...
\n\t*1. Crawling with your hands and feet
\t*2. Walk confidently across!""")

    nextmove = input("So 1 or 2: ")

    if nextmove == "1":
        print("\n Custodian: Ah Yes! The careful approach will assure your success!")
        time.sleep(2)
        print("\n You make it to the cup, but by the time you stand up...")
        time.sleep(2)
        victorious(name)
    else:
        print("\n Custodian: Your inability to see the best path laid out before you is why you failed")
        time.sleep(1)
        print("\n Custodian: To be honest, this is a fault common among your kind")
        time.sleep(1)
        if nextmove == "2":
            print("\nAs you walk confidently across the makeshift bridge\
 an unpredictably strong gust of hot wind lifts you off the ladder and head first\
 into the lake of lava")
            print("\nThe good news is that you went in head first")
            time.sleep(1)
            print("\n But obviously, You're dead!\n\n")
            exit(0)

def victorious(name):
    print("\n\t------------------------------------------")
    print("\t You have entered The Hall of Judgement")
    print("\t------------------------------------------")
    time.sleep(2)

    print("\n\n Custodian: Welcome Back! %s, I knew you could do it!" % name)
    time.sleep(2)
    print("\nCustodian: You've completed your trial, which required wisdom above\
 stupidity. As I mentioned, I am only the Custodian or Caretaker. Upon completion\
 of the trial, you have been granted powers you've never dreamed of experiencing!")
    time.sleep(2)
    print("\nCustodian: This is the last time we will speak! You are ready for the next\
chapter in your adventure!")
    time.sleep(2)
    print("\nCongratulations! You've WON!")
    time.sleep(2)
    print("\n\t------------------------------------------")
    print("\n\t    Stay Tuned for Part Two!!!!")
    print("\n\t------------------------------------------")
    exit(0)

def gamestart(name):
    print ("\n It's so nice to finally meet you, %s." % name)
    print ("\nShall we begin?")

    begin = input("\nBegin? Y or N: ")

    if begin == 'Y' or begin == 'y':
        time.sleep(1)
        print ("""\nExcellent attitude, %s! That will serve you
well in the trials to come!""" % name)
        time.sleep(1)
        print("Then allow me to explain where you are!")
        mainroom(name)
    elif begin == 'N' or begin == 'n':
        print("""Perhaps you should fix your attitude,
before entering the game next time""")
        print("Bye %s! We will meet again!\n *Sinister Laugh*" % name)
        time.sleep(2)
        print("\t****************")
        print("\t MuahAhahAhahAha")
        print("\t****************")
        exit(0)
    else:
        print("I hate nothing more than a waster of time")
        print("""The omnipotent voice Smites you for not being able
to answer a yes or no question""")
        exit(0)

def start():
    print("\n\t------------------------------------------")
    print("\t      Test of Might: Text Adventure Game")
    print("\t------------------------------------------\n")
    time.sleep(2)

    print("Mysterious Voice: Good Morning Sleepy Head!")
    time.sleep(1)
    print("\nYou must be groggy, but nevermind that. Welcome to your final trial")
    print("But before I explain the game, let's get started with your name.")

start()
playerone = input("\nType your name here: ")
gamestart(playerone)
