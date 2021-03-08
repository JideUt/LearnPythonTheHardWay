# Exercise 44
# LPTHW
# Inheritance vs. Composition
# Page 170 (PDF Page 187)

# Last exercise really got me... I loved how I could see how to use the classes
# but I felt a little bit lost when I was instructed to try on my own first
# I made sure to play around with the code a bit before moving onto the next
# exercise

# This exercise accurately describes Inheritance as the "dark forest" that no one
# should go in, yet, behind learning it is all the glory
# In the analogy used, Multiple Inheritance is the Evil Lizard Queen lurking in
# the dark forest. The only way to become a real programmer is to decapitate the
# evil queen and make it out of the forest alive

# Most uses for Inheritances can be simplified or replaced by Composition

# Inheritance
    # When one class will get most or all of its features from the parent (base)
    # class. Actions done on an instance of the child class will also be done on
    # the instance of the base class that is inherited from.

    # 3 kinds of specialization:
        # 1. Actions on the child imply an action on the parent
        # 2. Actions on the child override the action on the parent
        # 3. Actions on the child alter the action on the parent

# Implicit Inheritance Example
class Parent(object):

    def implicit(self):
        print("Parent implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()


#Override Explicitly Inheritance Example
class ParentOverride(object):

    def override(self):
        print("Parent override()")

class ChildOverride(ParentOverride):

    def override(self):
        print("CHILD override()")

father = ParentOverride()
daughter = ChildOverride()

father.override()
daughter.override()


# Alter Before or After Inheritance Example
class ParentAlter(object):

    def altered(self):
        print("Parent altered()")

class ChildAlter(ParentAlter):

    def altered(self):
        print("CHILD, Before Parent altered()")
        super(ChildAlter, self).altered() # call super using arguments ChildAlter
                                       # and self, then call altered() on what returns
        print("CHILD, After Parent altered()")

mom = ParentAlter()
stepson = ChildAlter()

mom.altered()
stepson.altered()
