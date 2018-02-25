# Creating a mapping of state to abbreviation

states = {'Oregon': 'OR',
          'Florida': 'FL',
          'California': 'CA',
          'New York': 'NY',
          'Michigan': 'MI'}

# Creating a basic set of states and cities in them

cities = {
     'CA': 'San Franscisco',
     'MI': 'Detroit',
     'FL': 'Jacksonville'
}

# adding some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities

print ("-" * 10)
print ("NY state has: ", cities['NY'])
print ('OR state has: ', cities['OR'])

#Print some states

print ("-" * 10)
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("Florida's abbreviation is: ", states['Florida'])

# Do it by using the state then cities dict
print ("-" * 10)
print ("Michigan has: ", cities[states['Michigan']])
print ("Florida has: ", cities[states['Florida']])

# Print every state abbreviations

print ("-" * 10)
for i,j in states.items():
    print ("%s is abbreviated as %s" % (i,j))

# Print every city in states

print ("-" * 10)
for i,j in cities.items():
    print ("The state %s has %s city" % (i,j))

# Now, do both at the same time

print ("-" * 10)
for i,j in states.items():
    print ("%s is abbreviated as %s and %s has %s city" % (i,j,j,cities[j]))

print ("-" * 10)
print ("safely get an abbreviation by state that might not be there")

state = states.get("Texas", None)

if not state:
    print ("Sorry, no Texas")

# Get a City with a default value

city = cities.get("TX", "Does not exits")
print ("The city for the state \"TX\" is %s" % city)
