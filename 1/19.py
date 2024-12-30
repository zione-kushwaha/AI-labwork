"""
Define classes Engine, Wheel, and Car. Engine and Wheel classes have attributes type and
methods start() and stop(). The Car class should have instances of Engine and Wheel classes
as attributes. Implement a method start_car() in the Car class which starts the engine and prints
"Car started"
"""


class engine:
    def __init__(self, type):
        self.type = type

    def start(self):
        print("engine started")

    def stop(self):
        print("engine stopped")


class wheel:
    def __init__(self, type):
        self.type = type

    def start(self):
        print("wheel started")

    def stop(self):
        print("wheel stopped")

class car:
    def __init__(self, engine, wheel):
        self.engine = engine
        self.wheel = wheel

    def start_car(self):
        self.engine.start()
        print("Car started")


e = engine('diesel')
w = wheel('good wheel')
c = car(e, w)
c.start_car();