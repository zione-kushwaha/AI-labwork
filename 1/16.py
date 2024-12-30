"""""
Define a class Vehicle with attributes make and model, and a method drive() which prints
"Driving the [make] [model]". Then, create a subclass Car that inherits from Vehicle and overrides
the drive() method to print "Driving the [make] [model] car".

"""

class vehicle:
    def __init__ (self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print("driving the", self.make, self.model)

class car(vehicle):
    def drive(self):
        print("driving the", self.make, self.model, "car")

v = vehicle('make', 'model')
v.drive()

c = car('make', 'model')
c.drive()