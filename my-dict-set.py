# create a mapping of states and their abbreviation


states = {
  'Oregon': 'OR',
  'Florida': 'FL',
  'New York': 'NY',
  'California': 'CA',
  'Michigan': 'MI'

}

# create a basic set of states and some cities in them

cities = {
  'CA': 'San Francisco',
  'MI': 'Detriot',
  'FL': "Miami"

}

# add more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print ('-' * 10)

print ("NY State has: ", cities['NY'])
print ("OR state has: ", cities['OR'])

# print some states

print ('-'* 10)
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("Florida's abbreviation is: ", states['Florida'])

print ('-'* 10)
for abbrev, city in cities.items():
    print ("%s has the city %s" % (abbrev, city ))

print ('-'* 10)
for state, abbrev in states.items():
    print ("%s state is abbreviated %s and has city %s" % (states, abbrev, cities[abbrev]))
