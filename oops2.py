# Inheritance
class Vehicle:
    def __init__(self,color,maxspeed):
        self.color = color
        self.__maxspeed = maxspeed  # it is private member
        # self.maxspeed = maxspeed
    def getMaxspeed(self):
        return self.__maxspeed
    def setMaxspeed(self,maxspeed):
        self.__maxspeed = maxspeed
    def print(self):
        print('Color :', self.color)
        # print('MaxSpeed :',self.maxspeed)
        print('MaxSpeed :', self.getMaxspeed())
class Car(Vehicle):
    def __init__(self,color,maxspeed,no_gears,isConvertible):
        super().__init__(color, maxspeed)
        self.no_gears = no_gears
        self.isConvertible = isConvertible

    def printCar(self):
        super().print()
        # self.print()
        print('No of gears :',self.no_gears)
        print('Is Convertible :',self.isConvertible)

C = Car('red',35,3,False)
C.printCar()

# Polymorphism
class Vehicle:
    def __init__(self,color,maxspeed):
        self.color = color
        self.__maxspeed = maxspeed  # it is private member
        # self.maxspeed = maxspeed
    def getMaxspeed(self):
        return self.__maxspeed
    def setMaxspeed(self,maxspeed):
        self.__maxspeed = maxspeed
    def print(self):
        print('Color :', self.color)
        # print('MaxSpeed :',self.maxspeed)
        print('MaxSpeed :', self.getMaxspeed())
class Car(Vehicle):
    def __init__(self,color,maxspeed,no_gears,isConvertible):
        super().__init__(color, maxspeed)
        self.no_gears = no_gears
        self.isConvertible = isConvertible

    # def printCar(self):
    def print(self):
        # super().print()
        # self.print()
        print('No of gears :',self.no_gears)
        print('Is Convertible :',self.isConvertible)

C = Car('red',35,3,False)
C.print()

V = Vehicle('black',500)
V.print()

# object Class

class Circle(object):
    def __init__(self,radius):
        self.radius = radius
    def __str__(self):
        return 'This is a circle class which takes radius as argument'

c = Circle(3)
print(c)


# Multiple Inheritance

class Mother:
    def __init__(self):
        self.name = 'Manju'
    def print(self):
        print('Print of Mother called')

class Father:
    def __init__(self):
        self.name = 'Ajay'
    def print(self):
        print('Print of Father called')

class Child(Father,Mother):
    def __init__(self):
        super().__init__()
    def printChild(self):
        print('Name of child is ', self.name )

C = Child()
C.printChild()
# Method order resolution
print(Child.mro())

# Operator overloading
import math
class Point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'This point is at ({self.__x},{self.__y})'
    def __add__(self,point_object):
        return Point(self.__x + point_object.__x,self.__y+point_object.__y)
    def __lt__(self,point_object):
        return math.sqrt(self.__x**2 +self.__y**2)  <  math.sqrt(point_object.__x**2 +point_object.__y**2)

p1  = Point(1,2)
p2  = Point(3,4)
p3 = p1+p2
print(p3)
print(p1<p2)






