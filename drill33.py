def number_p(x,y):
    i = 0
    numbers = []
    while i < x:
        print ("At the top of i is %d" % i)
        numbers.append(i)

        i = i+y
        print ("Numbers now: ", numbers)
        print ("At the bottom of i is %d" % i)
    print ("The numbers are: ")
    for num in numbers:
        print (num)

number_p(6,2)
