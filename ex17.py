from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("I am about to copy the contents from %s to %s" % (from_file, to_file))

in_file = open (from_file)
indata = in_file.read()

# the above two commands could have been accoplished in a single line too
# indata = read(open(from_file))

print ("The input file is %d bytes long" % len(indata))
print ("Does the output file exists? %r" % exists(to_file))

print ("Ready, hit RETURN to continue, CTRL-C TO abort")
input()

out_file = open (to_file, "w")
out_file.write(indata)

print ("Alright, all done")

out_file.close()
in_file.close()
