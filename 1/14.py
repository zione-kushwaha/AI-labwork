 #  Write a Python program to create a class representing a Circle. Include methods to calculate its area
 #  and perimeter.

class circle:
    def __init__(self, radius): 
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
c = circle(7)
print("area of circle is: ", c.area())
print("perimeter of crcle is: ", c.perimeter())
    