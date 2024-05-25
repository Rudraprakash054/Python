# Imports
from abc import ABC, abstractmethod, abstractproperty


#  Class(Employee) - Blueprint of a object
class Employee:
    pass


# Object(emp) - Instance of a class
emp = Employee()


# Parameterized Constructor, Because passing name param in init constructor
class Student:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


# Non-Parameterized Constructor, Not passing any params in init constructor
class Employee:

    def __init__(self):
        self.name = "Rudra Prakash"

    def get_name(self):
        return self.name


s1 = Student("Rudra")
e1 = Employee()
print("Parameterized constructor class:", s1.get_name())
print("Non Parameterized constructor class:", e1.get_name())


# Method overloading - It does not support in python
class Sum:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):  # Class uses the latest method
        return a + b + c


s = Sum()
print("Addition of 3 numbers:", s.add(1, 2, 3))


# Similar to method overloading
def sum(*args):
    result = 0
    for num in args:
        result += num
    return result


print(f"first addition: {sum(1, 2)}, second addition: {sum(1, 2, 4)}")


# Method overriding - Can implement on inheritance classes
class Family:

    def son(self):
        print("Base class son")


class Dad(Family):

    def son(self):
        print("Derived class son")


Family().son()
Dad().son()


class AbstractTestClass(ABC):
    """
    Abstract class - The class won't allow to create an object
    In python, we can't create a abstract but there is a default module in python(abc)
    """

    # class variable 
    greeting = "Hi, I'm ABSTRACT"

    def __init__(self) -> None:
        self.name = "Rudra Prakash"

    def __str__(self):
        return f'Hey, I am calling from inside abstract class {self.name}'

    @abstractmethod
    def check(self):
        pass

    @abstractproperty
    def get_name(self):
        return self.name


'''
Child class must implement the abstract method.
'''


class ChildAbstract(AbstractTestClass):

    # def __init__(self) -> None:
    #     super().__init__("Rudra Prakash")

    # def __str__(self):
    #     return super().__str__()

    def check(self):
        pass

    def get_name(self):
        return super().get_name


print(ChildAbstract())
# print(AbstractTestClass()) -> If we call this class throws an error


class Company:
    """
    Example of public, private and protect
    """
    def __init__(self, name, add, mobile_no):
        self.name = name  # Public - Access from anywhere
        self._add = add  # Protected - Access within the class and it's sub-class
        self.__mobile_no = mobile_no  # Private - Access within the class only

    def company_mobile_number(self):
        return f"Company Mobile Number: {self.__mobile_no}"


delhivery = Company("Delhivery", "Gurgaon", 9618732453)
print(f'Name: {delhivery.name}, Address: {delhivery._add}')

try:
    print(f'Mobile No: {delhivery.__mobile_no}')
except AttributeError:
    print("Error: You can't access private data members with objects, classes and outside of the class")
    # It returns mobile number, because private data members accessible inside the class
    print(delhivery.company_mobile_number())
