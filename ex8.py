formatter = "%r %r %r %r"
print (formatter % (1,2,3,4))
print (formatter % ("one", "two", "three", "Four" ))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))

# Python always tries to do best printing for you. Notice, the output of the
# Following lines. For some lines your output includes single quote while for
# other your output includes double quote. Becuase, notice here the first lines
# include one single qoute inside the double qoute string. hence, it qwill look
# weird if there is single as well as double qoute.

print (formatter % (
      "I'd this thing.",
      "That you could type up right.",
      "But it didn't sing.",
      "So I said goodnight.")
      )
