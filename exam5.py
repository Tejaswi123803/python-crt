#Program to check wheather a string is a palindrome
n=input()
if n==n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#Second largest element in a list
n=int(input())
arr=list(map(int,input().split()))
new_arr=[]
for num in arr:
    if num not in new_arr:
        new_arr.append(num)
    if len(new_arr)<2:
        print(-1)
    else:
        new_arr.sort()
        print(new_arr[-2])

#Python removing duplicates from tuple
n=int(input())
nums=list(dict.fromkeys(map(int,input().split())))
print(*nums)

#Exception Handling predict the output using EH
try:
    age=int(input("Enter the age: "))
    if age<18:
        raise ValueError;
    else:
        print("The age is valid")
except ValueError:
    print("The age is not valid")

#Product of array except self(LEETCODE PRBLM-238)
class Solution(object):
    def productExceptSelf(nums):
        n=len(nums)
        result=[1]*n
        left=1
        for i in range(n):
            result[i]*=right
            right*=nums[i]
            right=1
        for i in range(n-1,-1,-1):
            result[i]*=right
            right*=nums[i]
        return result