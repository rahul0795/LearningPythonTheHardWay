# Animal is-a object

class Animal(object):
    pass

# Dog is-a Animal
class Dog(Animal):
    def __init__(self,name):
        self.name = name

# Person "has-a"
class Person(object):
    def __init__(self,name):
        # Self has a name
        self.name = name
        # Self has a pet of some kind
        self.pet = None

# Employee is a Person
class Employee(Person):
    def __init__(self,name,salary):
        self.salary = salary
        super(Employee,self).__init__(name)

#
class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass


# rover is a Dog
rover = Dog('Rover')
#Satan is a cat
satan = Cat('Satan')
# Mary is a person
mary = Person('Mary')
# mary has a pet satan

mary.pet = satan

# Frank is a employee and has a salary of 120000
frank = Employee('Frank', 120000)
# Frank has a pet named rover
frank.pet = rover

# Flipper is a Fish
flipper = Fish()
# Crouse is a Salmon
crouse = Salmon()

harry = Halibut()
