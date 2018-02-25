from sys import argv

script, filename = argv

txt = open (filename)
print ("We are going to read the file %r" % filename)
print (txt.read ()) 
