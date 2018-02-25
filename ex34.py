from sys import exit

def gold_room():
    print ("This room is full of gold. How much do you take it?")
    next = input("> ")

    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, Learn to type a number.")

    if how_much < 50:
        print ("Nice, You are not greedy. You win")
        exit(0)
    else:
        print ("You greedy bastard")

def bear_room():
    print ("There is a bear there")
    print ("The bear has a bunch of money")
    print ("The fat bear is in from of another door")
    print ("How are you going to move the bear")
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey":
            dead("The bear looks at you and then slaps your face off")
        elif next == "taunt bear" and not bear_moved:
            print ("The bear has moved from the door and you can go through it now")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews you legs off")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")

def cthulhu_room():
    print ("Here, you see the great devil cthulhu")
    print ("He, it, whatever stares at you and you go insane")
    print ("Do you flee for your life or eat your head?")
    next = input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty")
    else:
        cthulhu_room()

def dead(why):
    print (why, "Goodjob")
    exit(0)

def start():
    print("You are in a dark room")
    print("There is a door to your right and left")
    print ("which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room untill you starve")

start()
