#1st code
def solve(n):
    full_crates = n // 12
    leftover_bottles = n % 12
    print("Full crates:", full_crates)
    print("Leftover bottles:", leftover_bottles)
n = int(input())
solve(n)

#2nd code
class Student:
    def _init_(self, student_id, student_name):
        self.id = student_id
        self.name = student_name
    def display(self):
        print(self.id)
        print(self.name)
if _name_ == "_main_":
    student_id_input = int(input())
    student_name_input = input()
    student = Student(student_id_input, student_name_input)
    student.display()

#3rd code
class Student:
    def _init_(self, student_id, student_name):
        self.id = student_id
        self.name = student_name
    def display(self):
        print(self.id)
        print(self.name)
if _name_ == "_main_":
    n = int(input()) 
    students = []
    for _ in range(n):
        student_id = int(input())      
        student_name = input()
        student = Student(student_id, student_name)
        students.append(student)
    for student in students:
        student.display()

#4th code
class Calculator:
    MULTIPLIER = 1  
    def calculate_square(self, number):
        return number * number
number = int(input())
calc = Calculator()
print(calc.calculate_square(number))

#5th code
def compute_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a, b = map(int, input().split())
print(compute_gcd(a, b))

#6th code
def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n
num = int(input())
print(digital_root(num))

#7th code
class Outer:
    def _init_(self, data):
        self.data = data
    class Inner:
        def _init_(self, outer_instance):
            self.outer_instance = outer_instance
        def display(self):
            print(f"Outer data: {self.outer_instance.data}")
n = int(input())
values = list(map(int, input().split()))
for value in values:
    outer = Outer(value)
    inner = outer.Inner(outer)
    inner.display()

#8th code
n = int(input()) 
square = n * n
digit_sum = sum(int(digit) for digit in str(square))
if digit_sum == n:
    print("Yes")
else:
    print("No")