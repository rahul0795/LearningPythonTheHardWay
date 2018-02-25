# The basic data related to the cars and passengers of the company
# Rahul Jha

cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

# The following is the summary of the above data of the carpool company
# Rahul Jha

print ("There are", cars , "cars available")
print ("There are only", drivers, "drivers available")
print ("There will be", cars_not_driven, "empty cars today")
print ("We can transport", carpool_capacity, "people today")
print ("We have", passengers, "to carpool today")
print ("We have to put about", average_passengers_per_car, "in each car")
