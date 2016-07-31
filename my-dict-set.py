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
