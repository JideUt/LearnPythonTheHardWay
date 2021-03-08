# Exercise 39
# LPTHW
# Dictionaries, Oh Lovely Dictionaries
# Page 132 (PDF page 149)

# Let's get into some Dictionaries
# "It is the most useful container ever"
# In other languages they are called hashes
# A unique feat. with dicts is being able to use anything to index through them
# the thing you use to call/index the dict is called a key
# you can delete things using the del keyword and then the key of what you want
    # deleted

# create a mapping of state to abbreviation

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

# create a basic set of states and some cities in them
cities = {'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print our some cities

print('-'*10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('-'*10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-'*10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbreviation
print('-'*10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

# print every city in state
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

# now do both at the same time
print('-'*10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))

print('-'*10)
#safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: %s" % city )
print('-'*10)


# Province and abbreviation
provinces = {
    'British Columbia': 'BC',
    'Alberta': 'AB',
    'Saskatchewan': 'SK',
    'Manitoba': 'MB'
}

# cities in provinces
can_cities = {
    'BC': 'Victoria',
    'AB': 'Edmonton',
    'SK': 'Saskatoon',
    'MB': 'Winnipeg'
}

# add some new cities
can_cities['ON'] = 'Toronto'
can_cities['QE'] = 'Montreal'

# add some provinces and abbreviations
provinces['Ontario'] = 'ON'
provinces['Quebec'] = 'QE'

#print it all!
for province, abbrev in provinces.items():
    print('--'*10)
    print("%s is abbreviated to %s and it's most popular city is %s." % (
    province, abbrev, can_cities[abbrev]) )

findinfo = can_cities.get('NV', 'This was not found')
print('-'*20)
print(findinfo)
#Using the Get Method, you can place a default message if key is not in the dict
# If it is in the dict, the corresponding value will show
