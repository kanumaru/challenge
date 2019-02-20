class Apple:
    def __init__(self,k,w,c,f):
        self.kind = k
        self.weight = w
        self.cllor = c
        self.famous = f
import math
class Circle:
    def __init__(self,r):
        self.radius  = r
    def calculate_area(self):
        print(self.radius**2 * math.pi)#piメソッドにかっこはいらない
class Triangle:
    def __init__(self,h,b):
        self.height = h
        self.base = b
    def calculate_area(self):
        return self.height * self.base / 2
class Hexagon:
    def __init__(self,s1,s2,s3,s4,s5,s6):
        self.sides = [s1,s2,s3,s4,s5,s6]
    def calculate_perimeter(self):
        print(sum(self.sides))
        
