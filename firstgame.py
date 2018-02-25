# This is my first game that i created after completing first 35 exercises of
# the PYTHON THE HARD WAY - BY ZEN SHAW

from sys import exit

def start():
    print ("Hello, Welcome to the world of Zumanji")
    print ("To enter this world, you have three doors")
    print ("Door.1\nDoor.2\nDoor.3")
    print ("The Door will be chosen by entering a number and you will taken to one of the world randomly")

    print ("Are you ready to enter a number?")
    ready = input (">")
    if int(ready) <= 10:
        print ("You entered a number less than 10, so we are going to first room")
        print ("There are so many suprises for you in this room. All the best")
        Door_1()
    elif int(ready) > 10 and int(ready) <= 30:
        print ("You seem to like numbers from 10 to 30, so we are going to the second room")
        print ("It is one of the most dreaded rooms of the Zumanji. All the best.")
        Door_2()
    else:
        print ("Welcome to the room three, you have entered a number greater than 30")
        print ("ALL THE BEST")
        Door_3()

def Door_1():
    print ("Wecome to the first door of the Zumanji")
    print ("In this door, you will meet a great a devil called MONA")
    print ("Do you want to meet MONA. Enter Y for Yes and N for No")
    meet = input ("> ")
    if meet == "Y":
        print ("HAHAHA, I am the great DEVIL of the Door1. Why have you come here?")
        print ("""
        1. Kill Me
        2. Want to stole my Treasures
              """)
        purpose = input("> ")
        if purpose == "1":
            print ("You bastard, you are here to kill me")
            print ("I am going to eat your ass off")
            print ("The MONA Devil eats you alive and you lose the game")

        else:
            print ("You have only one chance to snatch the Treasures of MONA")
            print ("You want to hit MONA on head or on penis")
            hit = input("> ")
            if hit == "head":
                print ("The Monster picks you hand and eats you alive")
            elif hit == "penis":
                print ("The Monster stumbles and you snatch the Treasuresof the MONA. You Won")
    elif meet == "N":
        start()
    else:
        print ("You bastard, are you kidding with me")
        exit(0)

def Door_2():
    print ("Hello, User How are you?")
    print ("What is your great name?")
    print ("The first letter of your name will decide whether you are going to survive or not")
    print ("If your name starts with the Vowel, then you will loop around this game")
    print ("Enter your name")
    name = input("> ")
    if name[0] in ("A", "E", "I", "O", "U"):
        Door_2()
    else:
        Door_3()
def Door_3():
    print ("Hmmm, So are finally here.")
    print ("I have waiting for someone from the last 2500 years")
    print ("If you give correct answers to my questions, then you are going to exit from this game")
    print ("Otherwise, probably you are going to exit this game")

    print ("Ok, now tell me what do you think the 23 + 24 / 2 is?")
    answer = input("> ")
    if int(answer) == 35:
        start()
    elif int(answer) == 23:
        Door_1()
    else:
        print ("Oh, my go you found it. You are now free. You have given the wrong answer and that what i wanted")
        exit(0)

start()
