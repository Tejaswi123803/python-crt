#Sort a dictionary by keys
n=int(input())
data={}
for _ in range(n):
    name,score=input().split()
    data[name]=int(score)
    for name in sorted(data):
        print(f"{name}:{data[name]}")

#Squares of even numbers using list comprehension
n=int(input())
arr=list(map(int,input().split()))
squares=[x*x for x in arr if x%2==0]
print(*squares)

#Find minimum and maximum in a set
n=int(input())
num=list(map(int,input().split()))
print("Minimum elements:", min(num))
print("Maximum elements:", max(num))

#Sum all values in a dictionary
n=int(input())
data={}
for _ in range(n):
    name, score = input().split()
    data[name] = int(score)
print(sum(data.values()))

#Python program to find tuples which have all elements divisible by k from a list of tuples
n = int(input())
list = [tuple(map(int, input().split())) for _ in range(n)]
k= int(input())
for t in list:
    if all(x % k == 0 for x in t):
        print(*t)