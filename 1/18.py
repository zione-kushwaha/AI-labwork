"""""
Implement a class Shape with a method area() which returns 0. Then, create subclasses
Rectangle and Circle. Overload the area() method in both subclasses to calculate and return
the area of a rectangle and a circle respectively

"""

class shape:
    def area(self):
        return 0

class rectangle(shape):
    def __init__(abc, l, b):
        abc.l = l
        abc.b = b

    def area(abc):
        return abc.l * abc.b 
    
class circle(shape):
    def __init__(abc, r):
        abc.r = r

    def area(abc):
        return 3.14 * abc.r * abc.r

rec = rectangle(5, 10)
print("area of the rectange is: ", rec.area())


cir = circle(7)
print("area of the circle is: ", cir.area())