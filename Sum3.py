#Python program to find the second largest number
n=int(input())
arr=list(map(int,input().split()))
first=second=float('-inf')
for num in arr:
    if num>first:
        second=first
        first=num
    elif first>num>second:
        second=num
print(second)
