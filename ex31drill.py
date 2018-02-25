print ("To play, this game. Most of theb question are in the for of Yes or No. Lets do a quick demo")
print ("Press Y for Yes and N for No")
test = input(">")
if test == "Y" or test == "N":
    print ("You are ready. Go ahead")
else:
    print ("Sorry, you cannot press these kinds of keywords")


print ("You have to Complete this mission\n")
print ("It's a matter of nation\n")
print ("Do you really want to save this country? Enter Yes, if you want. If No, you can type No")

do_you = input (">")

if do_you == "Yes":
    print ("I am glad that you took intrest in this cause of nation.\n")
    print ("Are you ready for the mission. Y/N")
    ready = input (">")
    if ready == "Y":
        print ("I had expected this from you\n")
        print ("Ok, So my self RAHUL JHA and you?\n")
        name_agent = input (">")
        print ("Nice to meet you %s" % name_agent)
        print ("Remaining talking, we will do later\n")
        print ("%s, what do you know about the terrorist and what are their hiding location. Tell me everything" % name_agent)
        print ("ok, how many persons you want with you")
        print ("1. Two\n 2. Three\n 3. None")
        how_many = input (">")
        if how_many == "1" or how_many == "2":
            print ("Ok, i will arrange the men")
        else:
            print ("You are really a brave boy who want to fight for the cause of the country")
        print ("Hey, what is the report. Do you think you saved the nation. Y/N")
        saved = input (">")
        if saved == "Y":
            print ("I knew it. You saved your nation from such a disatrous event")
            print ("You really deserves a medal")
            print ("How about appointing you as a commandant officier. Are you intrested.")
            officier = input ()
            if officier == "Y":
                print ("I am glad to hear that. Now, we will demolish the terrorists together")
            else:
                print ("It's alright. No problme. You have already achived this great feat by killing those terrorists")

        else:
            print ("You did your best to save the country and hurry up and tell the location of the terrorists, so we can send the team to capture those terrorists")

    else:
        print ("Then, why did you choose yes earlier. Do not waste our time in case of such urgency")

elif do_you == "No":
    print ("Thank you for at least taking intrest in it.")

else:
    print ("I have not expected this from you. This is a matter of death\nand you are wating our time by entering wrong keys. Only  \"Yes\" or \"No\" is applicable. \n Thank you")
