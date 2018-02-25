from sys import argv

# The following line of code tells the python that while running it from
# shell, how many arguments we are going to use. the first argument is the user_name
# of the script and second argument is the name of the user. The third arguments
# can be anything. If, we had script, user_name = argv, then while running the
# the script from the power shell, we only have to pass two arguments
# to run the script.

script, user_name, false = argv
prompt = "****"

print ("Hi %s, I'm %s script." % (user_name, script))
print ("I'd like to ask you a few questions.")
print ("Do you like me %s?" % user_name)

likes = input (prompt)

print ("Where do you live %s?" % user_name)
lives = input (prompt)

print ("What Kind of computer do you have?")
computer = input (prompt)

print ("""
Alright, so you said %r about liking me,
You live in %r. Not Sure, where it is.
And, you have a %r computer. Very Nice.
And, one more thing, Thank you for sharing your information with me.""" % (likes, lives, computer))
