#1)Read two integers from numerator and denominator
try:
    numerator = int(input())
    denominator = int(input())
    result = numerator // denominator
    print(result)
except ZeroDivisionError:
    print("Division by zero is not allowed")


#2)Use tuple and give the max
T = int(input())
E = list(map(int, input().split()))
L = list(map(int, input().split()))

max_guests = 0
current_guests = 0

for i in range(T):
    current_guests += E[i] - L[i]
    if current_guests > max_guests:
        max_guests = current_guests

print(max_guests)


#3)Find the Invalid age through exception handling
class InvalidAgeException(Exception):
    def _init_(self, message="Age must be 18 or older"):
        super()._init_(message)

def validate_age(age):
    if age < 18:
        raise InvalidAgeException("Age must be 18 or older")
    print("Access granted")

try:
    age = int(input())
    validate_age(age)
except InvalidAgeException as e:
    print(f"InvalidAgeException: {e}")
except ValueError:
    print("Invalid input: Please enter a valid integer for age.")


#4)Find the Invalid pin using exception handling
class InvalidPinException(Exception):
    def _init_(self, message="Incorrect PIN entered"):
        super()._init_(message)

def validate_pin(pin):
    if pin != 1234:
        raise InvalidPinException()
    print("Access granted")

try:
    pin = int(input())
    validate_pin(pin)
except InvalidPinException as e:
    print(f"InvalidPinException: Invalid PIN granted. {e}")
except ValueError:
    print("Invalid input: Please enter a valid integer for PIN.")


#Check validity and print result
import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}$"
    return re.match(pattern, email) is not None

email = input()

if is_valid_email(email):
    print("Invalid Email")
else:
    print("Valid Email")