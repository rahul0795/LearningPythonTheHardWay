# The following variable intializes the variable x which holds a string
x = "There are %d types of people in the world." % 10

#Further, we introduces two new variable binary and do_not.
binary = "binary"
do_not = "Don't"

# the following y takes a string and embedd two string
y = "Those who know %s and those who %s" % ( binary , do_not)

# The following command prints the variable x and y that we have craeted so far
print (x)
print (y)

# Notice, the below command, it uses the formaatters %r to print a string
# character. So, what does that mean, it mean that no matter what, it will
# print that object in the right

print ("I said: %r" % x)
print ("I also said: %s" % y)

# The following command declares two variable and notice the end of the second variable


hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Notice, how the end of the joke_evaluation works in the following command

print (joke_evaluation % hilarious)

# The declareation of the following two variables that takes two strings


w = "This is the left side of..."
e = "a string with a right side."

# The following command runs concatenates that two strings

print (w + e)
