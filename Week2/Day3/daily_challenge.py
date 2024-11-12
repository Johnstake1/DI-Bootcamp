#Daily Challenge
import math as m

class Circle:
    def __init__(self, radius, diameter):
        if radius > 0:
            self.radius = radius
            self.diameter = 2 * radius
        elif diameter >= 0:
            self.diameter = diameter
            self.radius = diameter / 2
    def area(self):
        self.surface = m.pi * (self.radius **2)
        return self.surface
    def __str__(self):
        return f'The circles radius is {self.radius}, its diameter is {self.diameter}, and its area is {self.surface}'
    
    def __add__(self, other):
        if isinstance(other, Circle):
            self.radius += other.radius
            return self
    def __gt__(self,other):
        if isinstance(other, Circle):
            return self.radius >= other.radius
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius



        
c1 = Circle(radius=0, diameter=3)
print(c1.radius)
print(c1.diameter)
print(c1.area())

c2 = Circle(radius=0, diameter=2)

c3 = c1 + c2
print(c3) #why i does not show the print of c3??
    
