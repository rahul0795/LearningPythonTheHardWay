class scene(object):
     def __init__(self, user,false ):
         self.user = user

     def door_1(self):
        print ("Wecome", self.user, "This is the first door of the jungle\n" )
        print ("What is your next move? Would you hit or dodge?")
        move = input("> ")
        if move == "hit":
            print ("You dare to hit me, ahhhhaa. You won. Good Job")
        elif move == "dodge":
            print ("You should have hit me. Now Rest in peace. Bammmm")
            print ("The Monster killed you by his hammer")
        else:
            print ("You fell into a khai or endless abyss")

play = scene("Rahul", "g")
play.door_1()
