from sys import argv

script, from_file, to_file = argv

# The following command is hard one. You have see it through. it replaces the burden of doing things two
# things that is done inside the two comments written below the following command.
# If you have to see the even longer method, then you can go and visis your ex17.py script.

open(to_file, "w").write(open(from_file).read())

# indata = open (from_file).read()

# open (to_file, "w").write(indata)
