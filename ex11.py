print ("How old are you?",)
age = input()
print ("How tall are you?",)
height = input()
print ("How much do you weigh?",)
weight = input()

# There is a difference between input() and raw_input(). the former is for
# python 3 and the latter is in python 2.

print ("So, you are %r old, %r tall and %r heavy." % (age, height, weight))
