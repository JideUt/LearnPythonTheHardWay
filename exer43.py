# Exercise 43
# LPTHW
# Basic Object-Oriented Analysis and Design
# Page 156 (PDF Page 173)

# This exercise is a guideline of what path to follow when building something
    # with Python
# Guideline/ Process
    # 1. Write or draw about the problem
    # 2. Extract key concepts from #1 and research them
    # 3. Create a class hierarchy and object map for the concepts
    # 4. Code the classes and a test to run them
    # 5. Repeat and refine
# the above guideline will not always work but gives a starting point
#  A Top-Down approach, starting from the abstract and working towards implementation
# I've ignored note taking and commenting up to this point
# I've ignored planning up until this point
# This is potentially the most important thing for me to Practice

# Start Coding for #Gothons from Planet Percal #25
    # Using the process above, top down

# “Aliens have invaded a space ship and our hero has to go through a maze of
# rooms defeating them so he can escape into an escape pod to the planet below.
# The game will be more like a Zork or Adventure type game with text outputs and
# funny ways to die. The game will involve an engine that runs a map full of rooms
# or scenes. Each room will print its own description when the player enters it
# and then tell the engine what room to run next out of the map.”

# Next, list out all nouns and verbs to start general idea of mapping out
# what classes, objects and functions you need
#
# * Alien
# * Player
# * Ship
# * Maze
# * Room
# * Scene
# * Gothon
# * Escape Pod
# * Planet
# * Map
# * Engine
# * Death
# * Central Corridor
# * Laser Weapon Armory
# * The Bridge

# Next, A class hierarchy by asking what is similar, what is the same, and how
    # do they relate?

# * Map
# * Engine
# * Scene
#     * Death
#     * Central Corridor
#     * Laser Weapon Armory
#     * The Bridge
#     * Escape Pod

# Next, ad the actions needed for each class/noun to map out how it will work or
    # transition

# * Map
#     - next_scene
#     - opening_scene
# * Engine
#     - play
# * Scene
#     - enter
#     * Death
#     * Central Corridor
#     * Laser Weapon Armory
#     * The Bridge
#     * Escape Pod
# * Character
#     * Alien
#     * Player

import sys
import time
import random

class Scene(object):

    def __init__(self):
        pass

    def enter(self):
        print("This class is common to all scenes. Subclass it and implement enter()")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print("Initializing Scenario")
        time.sleep(2)
        print("....")
        time.sleep(1)
        print("\n--------")
        print("\n\t\tGame Start")

        while True:
            print("\n--------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Character(object):

    def __init__(self):
        pass

class Player(Character):

    pass

class Alien(Character):

    pass

class Death(Scene):

    quips = [
    "You died. I didn't expect any more from you.",
    "Your mom would be proud... if she were any smarter.",
    "Wow, you really aren't good at this, are ya?",
    "The good news is my daughter wants to play next anyways. The bad news is you\
dead!"
    ]

    def enter(self):
        print(Death.quips[random.randint(0, len(self.quips)-1)])
        exit(1)

class Finished(Scene):

    def enter(self):
        time.sleep(1)
        print("\n--------------")
        print("That's it! You won!")
        time.sleep(1)
        print("\nThanks for playing my game that I copied from a textbook!")
        print("\n--------------")
        exit(0)

class CentralCorridor(Scene):


    def enter(self):
        print("""The Gothons of Planet Percal #25 have invaded your ship and killed
your entire crew. You are the last surviving member and your last mission is to
get the neutron destruct bomb from the Weapons Armory, put it in the bridge, and
blow the ship up after getting into an escape pod.
\n
You're running down the central corridor to the Weapons Armory when a Gothon jumps
out, red scaly skin, dark grimy teeth, and evil clown costume flowing around his
hate filled body. He's blocking the door to the Armory and about to pull a Weapon
to blast you!
""")

        action = input(">  ")
        if action == "shoot!":
            print("Quick on the draw, you yank out your blaster and fire at the\
Gothon.")
            print("His clown costume is flowing and moving around his body, which")
            print("throws off your aim. Your laser hits his costume but misses him.")
            print("This completely ruins his brand new costume his girlfriend\
bought him, which makes him fly into a rage and blast you repetedly in the face")
            print("until you die... Then he eats you.")
            return('death')

        elif action == "dodge!":
            print("Like a world class boxer, you dodge, weave, slip and slide")
            print("right as the Gothon's blaster cranks a laser past your head.")
            print("In the middle of your artful dodge your foot slips and you")
            print("bang your head on the metal wall and pass out.")
            print("You wake up shortly after only to die as the Gothon curb stomps")
            print("your face... And he starts eating you immediately.")
            return('death')

        elif action == "tell a joke":
            print("\nLucky for you they made you learn Gothon insults in the Academy.")
            print("You tell the one Gothon joke you know:")
            print("'Lbhe zbgure vf fb sng, jura fur fvgy nebhaw gur ugbhf, fur fcfgr!'")
            print("The Gothon stops, holding in a laugh, until he cannot contain it.")
            print("While he's frozen, laughing, you run up to him and shoot him \
point blank in the head and twice in the chest.")
            print("You've taken care of that Gothon and you head into the Weapon Armory.")
            return('laser_weapon_armory')

        else:
            print('DOES NOT COMPUTE')
            return('central_corridor')

class LaserWeaponArmory(Scene):

    def enter(self):
        print("You do a dive roll into the Weapon Armory, crouch and scan the room")
        print("for more Gothons that might be hiding. It's dead quiet, too quiet.")
        print("You stand up and run to the far side of the room and find the")
        print("neutron bomb in its container. There's a keypad lock on the box")
        print("and you need the code to get the bomb out. If you get the code wrong\
10 times, then the lock closes forever and the automatic defense system starts.")
        print("The code is 3 digits.")

        code = "%d%d%d" % (random.randint(1,9), random.randint(1,9), random.randint(1,9))
        guess = input("[Keypad]> ")
        guesses = 1
        cheat = "9999"

        while guess != cheat and guess != code and guesses < 10:
            print("BZZZZPT, INCORRECT PASSCODE")
            guesses += 1
            guess = input("[Keypad]> ")
            if guesses == 2:
                print("The first digit is %s" % code[0])
            elif guesses == 5:
                print("The second digit is %s" % code[1])
        if guess == code:
            print("The container seal opens up and the container clicks open\
releasing a white gas")
            print("You grab the neutron bomb and run as fast as you can to the")
            print("bridge where you must place it in the right spot!")
            return('the_bridge')
        elif guess == cheat:
            print("Wowwwww! You cheater, go ahead then! Get the bomb and leave!")
            time.sleep(2)
            return('the_bridge')
        else:
            print("BZZZPT, NO MORE ATTEMPTS")
            print("The lock buzzes one last time and then you hear a sickening")
            print("melting sound as the mechanism fuses together.")
            print("You decide to sit there in disbelief. The Gothons finally find")
            print("you and transport off the ship so they can blow up your ship\
with you aboard. You die!")
            return('death')

class TheBridge(Scene):

    def enter(self):
        print("You burst onto the Bridge with the neutron destruct bomb under your")
        print("arm and surprise 5 Gothons who are trying to take control of the")
        print("ship. Each of them has an even uglier clown costume than the last.")
        print("They haven't pulled their weapons out yet, as they see the active")
        print("bomb under your arm and don't want to set it off.")

        action = input("> ")

        if action == "throw the bomb":
            print("Panicked, you throw the bomb at the group of Gothons")
            print("and make a leap for the door. Right as you drop it a Gothon")
            print("shoots you right in the back, killing you.")
            print("As you are dying slowly, you see another Gothon frantically")
            print("trying to disarm the bomb. It brings you peace knowing that")
            print("they will all probably die with you when it goes off")
            return('death')

        elif action == "slowly place the bomb":
            print("You point your blaster at the bomb under your arm and the")
            print("Gothons take their hands off their guns. They're sweating.")
            print("You inch backward to the door, open it, and then carefully")
            print("place the bomb on the floor, pointing your blaster at it.")
            print("You then jump back through the door, punch the close button")
            print("and blast the lock so the Gothons can't get off the bridge!")
            print("Now that the bomb is placed you run to the escape pod to")
            print("get off this tin can.")
            return('escape_pod')
        else:
            print('DOES NOT COMPUTE!')
            return('the_bridge')


class EscapePod(Scene):

    def enter(self):
        print("You rush through the ship desperately trying to make it to the")
        print("escape pod before the whole ship explodes. It seems like hardly")
        print("any Gothons are on the ship, so your run is clear of interference.")
        print("You get to the chamber with the escape pods, and now you need to")
        print("pick one to take. Some of them could be damaged from the initial")
        print("attack but you don't have time to look. There are 5 pods, which one")
        print("do you take?")

        good_pod = str(random.randint(1,5))
        guess = input("[Pod #]> ")
        cheater = 'you choose!'

        if guess != good_pod and guess != cheater:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod escapes out into the void of space, then you hear a")
            print("crack, right before the hull implodes and crushes your body.")
            print("Before you can react, your body is smoothened out into a")
            print("paste. Yes, you're dead.")
            return('death')

        elif guess == cheater:
            time.sleep(1)
            print("\nAnother 4th Wall break, huh...")
            print("\n---------")
            time.sleep(1)
            print("FINE!!!")
            time.sleep(1)
            print("You jump into pod %s and hit the eject button." % good_pod)
            print("The pod easily slides out into space heading to the planet")
            print("below. As it flies to the planet, you have a clear view of")
            print("the ship. You see it implode and then instantaneously explode.")
            print("It reminds you of the first supernova you observed at the")
            print("Academy. You smile because you just took care of the Gothons")
            print("on your ship and got justice for your crewmates. You win!")

            return('finished')
        else:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod easily slides out into space heading to the planet")
            print("below. As it flies to the planet, you have a clear view of")
            print("the ship. You see it implode and then instantaneously explode.")
            print("It reminds you of the first supernova you observed at the")
            print("Academy. You smile because you just took care of the Gothons")
            print("on your ship and got justice for your crewmates. You win!")

            return('finished')

class Map(object):

    scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
