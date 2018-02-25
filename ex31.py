print ("You enter a dark room with only two doors. Do you go through the doors #1 or door #2")

door = input (">")

if door == "1":
    print ("There is a giant bear here eaating a cheese cake. what do you do?")
    print ("1. Take the cake")
    print ("2. Or, just scream at the bear")

    bear = input (">")

    if bear == "1":
        print ("The bear eats your face off. Good Job!")
    elif bear == "2":
        print ("The bear eats your legs off. Good Job!")
    else:
        print ("Well, Doing %s is probably better. Bear runs away" % bear)

elif door == "2":
    print ("You stare into the endless abyss at cthulhu's retina")
    print ("1. Blueberries")
    print ("2. Yellow jackets clothpins")
    print ("3. Understanding revolvers yelling melodies")

    insanity = input (">")

    if insanity == "1" or insanity == "2":
        print ("Your body survives powered by a mind of jello. Good job!")
    else:
        print ("The insanity rots your eyes into the pool of the muck. Good job!")

else:
    print ("You stumble around and fall on a knife and die. Good job!")
