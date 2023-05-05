# abstraction
from abc import ABC, abstractmethod
class Automobile(ABC):
    def __init__(self,no_of_wheels):
        print('Automobile created')
        self.no_of_wheels = no_of_wheels
    @abstractmethod
    def start(self):
        print('Start of Automobile')
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def drive(self):
        pass
    @abstractmethod
    def getNoOfWheels(self):
        return self.no_of_wheels
class Car(Automobile):
    # def __init__(self,name):
    #     print('Car created')
    #     self.name = name
    def start(self):
        print('Start of Car')
    def stop(self):
        pass
    def drive(self):
        pass
    def getNoOfWheels(self):
        return super().getNoOfWheels()
class Bus(Automobile):
    # def __init__(self,name):
    #     self.name = name
    #     print('Bus created')
    def start(self):
        pass
    def stop(self):
        pass
    def drive(self):
        pass

    def getNoOfWheels(self):
        return super().getNoOfWheels()
c = Car(4)
print(c.getNoOfWheels())
b = Bus(6)
print(b.getNoOfWheels())

#----------------------------------------------
# Errors and Exceptions
'''
Syntax Error
Zero Division Error
Name Error
Type Error
'''


try:
    n = input('Enter the numerator :')
    num = int(n)
    n = input('Enter the denominator :')
    den = int(n)
    value = num/den
    print(value)

except ValueError:
    print('Numerator And Denominator should be integer')
except ZeroDivisionError:
    print('Denominator should not be zero')
except (ValueError,ZeroDivisionError):
     print('Numerator And Denominator should be integer')
except Exception as e:
    print(e)

# Raise your Errors

class ZeroDemoniatorError(Exception):
    pass

try:
    n = input('Enter the numerator :')
    num = int(n)
    n = input('Enter the denominator :')
    den = int(n)
    if den ==0:
        raise ZeroDemoniatorError('Denominator should not be zero')
except ValueError:
    print('Numerator And Denominator should be integer')
except ZeroDivisionError:
    print('Denominator should not be zero')
except ZeroDemoniatorError:
    print('ZeroDenominatorError is raised')
# else and finally
else:
    value = num / den
    print(value)
finally:
    print(num)
    print(den)
    print(value)
    print('it will always execute whether Exception may or may not be raised')
