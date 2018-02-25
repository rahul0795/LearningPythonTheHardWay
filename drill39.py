states = {
"Uttar Pradesh": "UP",
"Bihar": "BH",
"New Delhi": "ND",
"Gujrat": "GU",
"Maharastra": "MH"
}

cities = {
"UP": "Luckhnow",
"BH": "Patna",
"GU": "Ahmedbad",
"MH": "Mumbai",
"ND": "Gurgaon"
}

for i,j in states.items():
    print ("%s : %s" % (i,j))

for i,j in cities.items():
    print ("%s : %s" %(i,j))

for i,j in states.items():
    print ("%s : %s" % (i,cities[j]))
