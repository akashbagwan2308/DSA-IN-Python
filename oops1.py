# hasattr()
# getattr()
#__dict__
#delattr() 


class Student:
    # name=''
    # rollnumber=12
    pass

s1 = Student()
s2 = Student()
s3 = Student()

s1.name='Akash'  # add data to class , it is a instance attribute
s2.rollnumber = 11
s3.name = 'Thor'
s3.rollnumber = 12
# print(s1.name,s3.rollnumber,s3.name)
# print(s2.name) #it will give an error
print(s1.__dict__) # it will give all attributes present for that instance
print(s2.__dict__) # it will give all attributes present for that instance
print(s3.__dict__) # it will give all attributes present for that instance
print(hasattr(s1,'name')) # it will check that particular attribute for that instance
print(hasattr(s2,'name')) # it will check that particular attribute for that instance
print(hasattr(s3,'name')) # it will check that particular attribute for that instance
print(getattr(s1,'name'))       # it will give the value of that instance attribute
print(getattr(s2,'rollnumber')) # it will give the value of that instance attribute
print(getattr(s3,'name'))       # it will give the value of that instance attribute
print(delattr(s1,'name'))         # it will delete that attribute from a particular instance
print(delattr(s2,'rollnumber'))   # it will delete that attribute from a particular instance
print(delattr(s3,'name'))         # it will delete that attribute from a particular instance
#--------------------------------------------------------------------------------------------


class Student1:
    PP = 80

s1= Student1()
s2 = Student1()
s2.PP= 70
print(s1.PP) # it will give the class attirbute bcz instance has nothing like PP
print(s2.PP)# if will give the instance class

#--------------------------------------------------------------------------------------------
# Self Parameter  and  static method (in which self is not passed)
# class method/factory method
# public and private access modifiers
from datetime import date
class Student2:
    pp = 40
    def __init__(self,name,age,percent):
        # self.name = name   # this is  public
        self.__name = name  # this is private
        self.age = age
        self.percent = percent

    def studentDetails(self): # instance method
        self.name = 'Akash'
        print("Name = ",self.name)
        # percentage = 80  # it is accessible inside this method only
        self.percentage = 80  #  now this can be accessible for instance throughout its life
        print("Percent = ",self.percentage)
        pass
    def isPassed(self):  # instance method
        if self.percentage>Student2.pp:
            print('Student ia passed')
        else:
            print('Student ia not passed')
    @staticmethod   # it if decorator
    def welcomeToSchool(): # it is a static method
       print('Hey! Welcome to School')
    @classmethod
    def birthday(cls,name,year,percent):
        return cls(name,date.today().year - year, percent)

    def studentdetails(self):
        print('Name', self.name)
        print('Age', self.age)
        print('Percent', self.percent)

# s1= Student2()
# s1.studentDetails()
# s1.isPassed()
# s1.welcomeToSchool()
s = Student2('Thor',2003,90)
# s =Student2.birthday('Akash',2000,89)
# print(s.studentdetails())
# s.name = 'Akash'
# print(s.__name)

#--------------------------------------------------------------------------------------------

# __init__ method
class Student3:
    def __init__(self,name,roll):
        self.name = name
        self.rollnum = roll

s1 = Student3('Akash',12)
print(s1.__dict__)
s2 = Student3('Gourav',13)
print(s2.__dict__)
#--------------------------------------------------------------------------------------------

class Fraction:
    def __init__(self,num=0,den=1):
        if den == 0:
            den = 1
        self.num = num
        self.den = den
    def print(self):
        if self.num ==0:
            print(0)
        elif self.den==1:
            print(self.num)
        else:
            print(self.num,'/',self.den)
    def simplify(self):
        if self.num == 0:
            self.den=1
            return
        current = min(self.num,self.den)
        while current>1:
            if self.num % current ==0 and self.den % current ==0:
                break
            current -=1
        self.num = self.num//current
        self.den = self.den//current
    def add(self,otherfraction):
        newNum = otherfraction.den*self.num + otherfraction.num * self.den
        newDen = self.den*otherfraction.den
        self.num = newNum
        self.den = newDen
        self.simplify()
    def multiply(self,otFraction):
        newNum = self.num*otFraction.num
        newDen = self.den*otFraction.den
        self.num = newNum
        self.den = newDen
        self.simplify()
# f = Fraction()
# print(f.__dict__)
# f1 = Fraction(0,3)
# print(f1.__dict__)
# f2 = Fraction(0,6)
# print(f2.__dict__)
# f2.simplify()
# f2.print()
# f1.print()
# f2.print()

f1 = Fraction(3,4)
f2 = Fraction(4,3)

# f1.add(f2)
# # f1.simplify()
# f1.print()

f1.multiply(f2)
f1.print()
#--------------------------------------------------------------------------------------------


class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def print(self):
        if self.real ==0:
            print(self.img,'i')
        elif self.img ==0:
            print(self.real)
        elif self.img<0:
            print(self.real,'-',abs(self.img),'j')
        else:
            print(self.real,'+',self.img,'j')
    def add(self,otcom):
        self.real = self.real+ otcom.real
        self.img = self.img+ otcom.img

    def multiply(self,otcom):
        newReal = self.real*otcom.real-self.img*otcom.img
        newImg = (self.img*otcom.real)+(self.real*otcom.img)
        self.real = newReal
        self.img = newImg


f1 = Complex(4,5)
f2 = Complex(6,7)
# f1.add(f2)
f1.multiply(f2)
f1.print()