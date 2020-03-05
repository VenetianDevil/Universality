#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
import math 

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Circle:
    """A class representing a circle"""

    def __init__(self, x=0, y=0, radius=1):
        if radius < 0:
            raise ValueError("negative radius")
        self.pt = Point(x, y)
        self.radius = radius
        
    def __repr__(self):       # "Circle(x, y, radius)"
        data = (self.pt.x, self.pt.y, self.radius)
        return ('Circle' + str(data))    

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius
    
    def __ne__(self, other):
        return not self == other
    
    def area(self):           # area
        return round(math.pi*self.radius*self.radius, )

    def move(self, x, y):     # shift by (x, y)
        return self.pt.x + x, self.pt.y + y

    def cover(self, other):   # circle covering both
        if (self.radius > other.radius):
            big = self
            small = other
        else:
            big = other
            small = self

        x = math.sqrt((self.pt.x - other.pt.x)*(self.pt.x - other.pt.x) + (self.pt.y - other.pt.y)*(self.pt.y - other.pt.y))
        if x < big.radius and small.radius <= big.radius - x:
            return big.radius, big.pt.x, big.pt.y
        else:
            new_R = (x + big.radius + small.radius)/2
            a = (big.pt.y - small.pt.y)/(big.pt.x - small.pt.x)
            b = big.pt.y - (big.pt.x) * a

            point1 = find_point_on_circle(a, b, big, small)
            point2 = find_point_on_circle(a, b, small, big)
            center = Point((point1.x - point2.x)/2, (point1.y - point2.y)/2)
            return new_R, center.x, center.y
            

    def find_point_on_circle(self, a, b, circle1, circle2):
        delta = (a*b - a*circle1.pt.y - circle1.pt.x)*(a*b - a*circle1.pt.y - circle1.pt.x) - 4 * (1 + a*a) * (circle1.pt.x*circle1.pt.x + b*b - 2 * b* circle1.pt.y + circle1.pt.y*circle1.pt.y - circle1.radius*circle1.radius)
        c1 = ((circle1.pt.x + a * circle1.pt.y - a*b) - math.sqrt(delta))/(2*(1 + a*a))
        pt_c1 = Point(c1, a*c1 + b)
        c2 = ((circle1.pt.x + a * circle1.pt.y - a*b) + math.sqrt(delta))/(2*(1 + a*a))
        pt_c2 = Point(c2, a*c2 + b)

        if (pt_c1.x - circle2.pt.x)*(pt_c1.x - circle2.pt.x)+(pt_c1.y - circle2.pt.y)*(pt_c1.y - circle2.pt.y) > (pt_c2.x - circle2.pt.x)*(pt_c2.x - circle2.pt.x)+(pt_c2.y - circle2.pt.y)*(pt_c2.y - circle2.pt.y):
            return pt_c1
        else:
            return pt_c2

r = int(input())
x, y = input().split()
c1 = Circle(int(x), int(y), r)
r = int(input())
x, y = input().split()
c2 = Circle(int(x), int(y), r)
x, y = input().split()

print (c1.area())
print (' '.join(map(str,c1.cover(c2))))
print (' '.join(map(str,c1.move(int(x), int(y)))))

