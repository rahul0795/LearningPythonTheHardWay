from sys import argv

script, filename = argv

print ("We are going to erase %r." % filename)
print ("If you do not want to do that, hit CTRL-C (^C).")
print ("If you want that, hit RETURN.")

input ("?")

print ("Opening the file...")
target = open (filename, "w")

print ("Truncating the file, Goodbye!")
target.truncate()

print ("Now, I'm going to ask you for some three lines")

line1 = input ("Line1 = ")
line2 = input ("Line2 = ")
line3 = input ("Line3 = ")

print ("Now, I am going to write these lines to the file.")

target.write (line1)
target.write ("\n")
target.write (line2)
target.write ("\n")
target.write (line3)
target.write ("\n")

print ("And, finally, we close it")
target.close ()
