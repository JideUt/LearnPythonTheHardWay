# Exercise 40
# LPTHW
# Modules, Classes, and Objects
# Page 138 (PDF page 155)

# So here we are, into the thick of it...
# Modules, Classes and Objects are probably my weakest points of python, if I
    # had to choose
# the last two weeks I spent making my text adventure game was only difficult
    # because I had to keep typing and it got boring but now I imagine
    # that what I learn here will help clean that code up
# class is a construct that lets you structure software in a particular way
# classes give consistency to your programs so they can be cleaner **In theory**
# Zed Shaw says you have to struggle with OOP, so this should be more diff.

# Very common pattern in Python is:
    # take a key=value style container
    # Get something out of it by the key's name
    # Example is how import module system is similar to dictionaries
    # In the case of a dict, key is a string
    # In the case of a module, key is an identifier

# dict style
    # mystuff['apples']
# module style
    # mystuff.apples()
    # print(mystuff.tangerine)
# class style
    # thing = MyStuff()
    # thing.apples()
    # print(thing.tangerine)

class Song(object):
    def __init__(self, lyrics): #Have to have the init and the self
        self.lyrics = lyrics
    def sing_me_a_song(self):
        print('*'*10)
        for line in self.lyrics:
            print(line)
        print('*'*10)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

jide_song = Song(["You are going to be a programmer",
                  "That is a guarantee",
                  "It's definitely very difficult",
                  "But you're happy as can be"])

jide_song.sing_me_a_song()

class Person(): # Don't put objects in here yet!!
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def who_is_this(self):
        print("Meet %s, they are %s years old, and %r tall" % (self.name, self.age, self.height))

jide = Person('Jide', '31', '72 inches')

jide.who_is_this()
