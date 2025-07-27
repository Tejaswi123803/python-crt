#Find the range(max-min) using args
def calculate_range(num):
    return max(num) - min(num)
num=list(map(int,input().split()))
print(calculate_range(num))

#Find maximum number usimg args
def find_maximum(*args):
    return max(args)
num=list(map(int,input().split()))
print(find_maximum(*num))

#Difference of sum
def difference_of_sum(n, m):
    nums = list(range(1, m + 1))
    sum_div = sum(x for x in nums if x % n == 0)
    sum_not_div = sum(x for x in nums if x % n != 0)
    return sum_not_div - sum_div

n = int(input())
m = int(input())

print(difference_of_sum(n, m))

#Count the digits of a number using recursive function
def count_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)
n = int(input())
print(count_digits(n))

#Character ASCII values
n=input()
ascii_dict={char:ord(char) for char in n}
ascii_map=", ".join([f"{char}:{ord(char)}" for char in ascii_dict])
print("{"+ascii_map+"}")

