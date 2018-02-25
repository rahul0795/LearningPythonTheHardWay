def add (a, b):
    print ("We are Going to add %d and %d..." % (a, b))
    return a + b

def subtract (a, b):
    print ("We are Going to subtract %d and %d..." % (a, b))
    return a - b

def multiply (a, b):
    print ("We are Going to multiply %d and %d..." % (a, b))
    return a * b

def divide (a, b):
    print (" we are going to the divide %d and %d..." % (a, b))
    return a / b

print ("Let's do some math with these functions...")

age = add (5, 18)
height = subtract (70, 5)
weight = multiply (13, 5)
iq = divide (100, 2)

print ("Age : %d\nheight : %d\nweight : %d\niq : %d" % (age, height, weight, iq))
