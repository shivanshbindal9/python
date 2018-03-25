class shape:
    pass

class rectangle(shape):

    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

    def area(self):
        return self.length*self.breadth

    def __str__(self):
        return 'Rectangle of length {} and breadth {}'.format(self.length,self.breadth)

class circle(shape):
    
    def __init__(self,radius):
        self.radius=radius

    def perimeter(self):
        return 2*3.14*self.radius

    def area(self):
        return 3.14*(self.radius**2)
    
    def __str__(self):
        return 'circle of radius {}'.format(self.radius)

class square(rectangle):

    def __init__ (self,side):
        self.length=side
        self.breadth=side

    def __str__(self):
        return 'Square of side {}'.format(self.length)
    

s1=rectangle(10,20)
s2=circle(5)
s3=square(20)

print (s1.area())
print (s2.perimeter())
print (s3.area())
print (s1)
print (s2)
print (s3)
