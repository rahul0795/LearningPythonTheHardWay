def cheese_and_crackers (cheese_count, boxes_of_crackers):
    print ("You have %d cheeses" % cheese_count)
    print ("You have %d boxes of crackers" % boxes_of_crackers)
    print ("Man, That's enough for the party")
    print ("Get a blanket\n")

print ("We can just give the function numbers directly:")
cheese_and_crackers (20, 30)

print ("Or, we can just use the variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers (amount_of_cheese, amount_of_crackers)

print ("We can even do math inside the function")
cheese_and_crackers (10 + 20, 5 + 6)

print ("Or, alternatively, you can also use the mix of the math and variable")
cheese_and_crackers (amount_of_cheese + 100, amount_of_crackers + 1000)

print ("A little bit of fun activity:")
print ("What is the number of cheeses you have:",)
cheeses_user = input ()
print ("Now, What is the number of boxes of crackers you have:",)
boxes_user = input ()

cheese_and_crackers (int (cheeses_user), int (boxes_user))
