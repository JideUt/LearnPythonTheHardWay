# Exercise 42
# LPTHW
# Is-A, Has-A, Objects, and Classes
#  Page 150 (PDF page 167)

# Learning the difference between a class and an object
# In truth there is no real difference
# Class is just a particular type of object
# In this lesson, I'll learn how to identify between a class and object
    # And the relationship between class and Objects
#Use is-a when objects and classes are related to eachother through a class
    # relationship
#Use has-a when objects and classes are related only because they reference each
    # other
# examples... is-a is the relationship between Fish and Salmon (two classes)
# has-a is the relationship between Salmon and Gills (class and object)
    # the salmon has Gills

## Animal is-a object
class Animal(object):
    def __init__(self):
        print("This is an animal")

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

        print(f"'Woof Woof' said {self.name}")

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name
        print(f"'Meow Meow' said {self.name}")

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

    def introduction(self):
        print(f"This is {self.name}")
        if self.pet is not None:
            print(f"and here is their pet {self.pet}")

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a name of Person
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

rover
satan
mary
frank.introduction()
