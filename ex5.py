# This is the 5th lesson and we will talk about format string

my_name = 'Rahul Jha'
my_age = 22
my_height = 65
my_weight_kg = 65
my_eyes = 'black'
my_teeth = 'While'
my_hair = 'Black'

print ("Let's talk about %s." % my_name)
print ("He is %d inces tall" % my_height)
print ("He weighes %d kilogram." % my_weight_kg)
print ("He has got %s hair and %s eyes." % (my_hair, my_eyes))
print ("He has %s white teeth depending upon whether he has brushed or not" % my_teeth)

# Here, you have to notice few things:
# First, notice here that %s, %d are used for embedding the strings and integer values
# in a strings. Also, note that after the end quote, there is not any comma.
# You can just proceed with % and then what the value embedded in the double
# quote refers to. To embedd two values in a single quotes, you have to put your
# values in the () seperated by the commas

# Notice, the following line of code. Specially, notice thnesequance, in which we
#PLace each of the component inside the strings

print ("If i add %d, %d and %d, I get %d" %(my_age, my_height, my_weight_kg,
my_age + my_height + my_weight_kg))
