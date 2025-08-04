# 
# Example 1
class Student:
    def _init_(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display(self):
        print(self.student_id)
        print(self.name)


def is_valid_id(student_id):
    return student_id.isdigit() and 1 <= int(student_id) <= 500

def is_valid_name(name):
    # Name should contain only letters and spaces (e.g., Aditi, Aditi Sharma)
    return all(part.isalpha() for part in name.strip().split())

try:
    n = int(input().strip())
    students = []

    for _ in range(n):
        student_id = input().strip()
        name = input().strip()

        if is_valid_id(student_id) and is_valid_name(name):
            students.append(Student(student_id, name))
        else:
            raise ValueError  # If any input is invalid, raise exception

    for student in students:
        student.display()

except:
    print("Invalid input")


#Example 2
class BankAccount:
    def _init_(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def display(self):
        print(f"{self.acc_no} {self.name} {self.balance}")


# Read input in one line
data = input().split()

# Parse input
acc_no = data[0]
name = data[1]
balance = float(data[2])
deposit_amt = float(data[3])
withdraw_amt = float(data[4])

# Create BankAccount object
account = BankAccount(acc_no, name, balance)

# Perform deposit and withdrawal
account.deposit(deposit_amt)
account.withdraw(withdraw_amt)

# Display result
account.display()


# Example 3
class Box:
    def _init_(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

    def volume(self):
        return self.height * self.width * self.depth


# Read input and split into integers
h, w, d = map(int, input().split())

# Create Box object and calculate volume
box = Box(h, w, d)
print(box.volume())


# Example 4
# Define a function to handle the logic
def generate_and_print_even_numbers(n):
    even_numbers = []

    if n > 0:
        # For positive n, generate even numbers from 2 up to n
        for num in range(2, n + 1, 2):
            even_numbers.append(num)
    elif n < 0:
        # For negative n, generate even numbers from -2 down to n
        for num in range(-2, n - 1, -2):
            even_numbers.append(num)
    
    # Print the numbers separated by spaces
    print(*even_numbers)

# Main part of the program
try:
    # Read the number from the user
    input_number = int(input())
    
    # Call the function to run the logic
    generate_and_print_even_numbers(input_number)

except ValueError:
    print("Invalid input. Please enter an integer.")


# Example 5
def find_sum_of_digits(n):
    n = abs(n)
    
    # Convert the number to a string to easily iterate through its digits
    n_str = str(n)
    
    # Initialize a variable to store the sum
    sum_of_digits = 0
    
    # Loop through each character (digit) in the string
    for digit_char in n_str:
        # Convert the character back to an integer and add to the sum
        sum_of_digits += int(digit_char)
        
    return sum_of_digits

# Main part of the program
if _name_ == "_main_":
    try:
        # Read the number from the user
        input_number = int(input())
        
        # Calculate the sum of the digits
        result = find_sum_of_digits(input_number)
        
        # Print the result in the specified format
        print(f"Sum is :{result}")
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")