class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius**2*3.14
    
c1 = Circle(5)
print(c1.area())