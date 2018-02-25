# The following command imports the sys library and takes the argv feature

from sys import argv

# the following intiatialization, describes the method by which, we are going to
# open the file from the terminal power shell
script, filename = argv

# the open() command opens the file with the name with the name file name'
txt = open (filename)

# the following line prints a little line that lets the users know that,
# file is going to be printed
print ("Here's your file %r:" % filename)
# the following command is actually amazing. Most of the work of the output is
# Done by the following command. the txt is the file and . is used to apply
# the command
print (txt.read())


print ("Type the fiile name again:")
file_again = input ("> ")

txt_again = open (file_again)

print (txt_again.read())
