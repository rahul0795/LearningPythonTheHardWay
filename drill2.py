from sys import argv
from os.path import exists

script, from_file, to_file = argv

file_from = open (from_file)
file_data = file_from.read()

file_to = open (to_file, "w")
file_to.write (file_data)

file_to.close()
file_from.close()
