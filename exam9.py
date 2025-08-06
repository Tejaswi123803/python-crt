# Duck Typing Example
class Animal:
    def sound(self):
        print("Animal Makes Sound")
class Dog:
    def sound(self):
        print("Barks")
class Cat:
    def sound(self):
        print("Meows")
def get_sound(animal):
    animal.sound()
get_sound(Dog())
get_sound(Cat())

#Type checking example
class Cat:
    def sound(self):
        print("Meows")
def self_sound(animal):
    if isinstance(animal, Cat) or isinstan
        animal.sound()
get_sound(Dog())
get_sound(Cat())

#Method overloading
class Math:
    def add(self,a=0,b=0,c=0,d=0):
        return a+b+c+d
m=Math()
print(m.add(2,3))
print(m.add(10,20))
print(m.add(20,30,40))
print(m.add(20,30,40,50))

#Method overriding
class Math:
    def add(self,a,b,c,d):
        return a+b+c+d
class AdvancedMath(Math):
    def add(self,a,b,c,d):
        return a+b+c+d
m=AdvancedMath()
print(m.add(10,20,30,40))

#Operation overloading
class Student:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,other):
        return self.marks+other.marks
    def __str___(self):
        return str(self.marks)
s1=Student(85)
s2=Student(90)
s3=Student(95)
s4=Student(100)
print(s1+s2+s3+s4)