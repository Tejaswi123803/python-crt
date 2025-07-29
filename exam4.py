#Program to check armstrong number
num=int(input())
original=num
digits=len(str(num))
total=0
while num>0:
    digit=num%10
    total+=digit**digits
    num//=10
print("true" if total==original else "false")

#Program to check if a given number in perfect numbers
n=int(input())
sum_divisors=0
for i in range(1,n):
    if n%i==0:
        sum_divisors+=i
if sum_divisors==n:
    print("Perfect")
else:
    print("Not Perfect")

# Automorphic numbers
n=int(input())
square=n*n
if str(square).endswith(str(n)):
    print("true")
else:
    print("false")

# Program to count the occurrences of each character
n = int(input())
s = input()

print("Character Occurrences:")
counted = set()

for char in s:
    if char not in counted:
        print(char, ":", s.count(char))
        counted.add(char)

# Reverse a string
n=int(input())
s=input()
reversed_string=s[::-1]
print(reversed_string)