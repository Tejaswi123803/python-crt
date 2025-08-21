#Example 1
n = int(input())
arr = list(map(int, input().split()))
if n < 2:
    print("-1 -1")
else:
    small = second_small = float('inf')
    large = second_large = float('-inf')
    for num in arr:
        # Update smallest and second smallest
        if num < small:
            second_small = small
            small = num
        elif small < num < second_small:
            second_small = num
        # Update largest and second largest
        if num > large:
            second_large = large
            large = num
        elif second_large < num < large:
            second_large = num
    if second_small == float('inf') or second_large == float('-inf'):
        print("-1 -1")
    else:
        print(f"{second_small} {second_large}")

#Example 2
s = input().strip()   # read input as a string
upper_count = sum(1 for ch in s if ch.isupper())
lower_count = sum(1 for ch in s if ch.islower())
if upper_count > lower_count:
    print(s.upper())
else:
    print(s.lower())

#Example 3
n = int(input())
experts = {}
for _ in range(n):
    topic, language = input().split()
    key = (topic, language)
    experts[key] = experts.get(key, 0) + 1
m = int(input())
unhappy_count = 0
for _ in range(m):
    topic, language = input().split()
    key = (topic, language)
    if experts.get(key, 0) > 0:
        experts[key] -= 1
    else:
        unhappy_count += 1
print(unhappy_count)

#Example 4
def oddOccurance(array):
    result=0
    for num in array:
        result ^= num
    return result
n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
print("Enter the total number of elements in an array")
print("Enter the value of elements in an array")
print(f"The element occuring odd number of times is {oddOccurance(arr)}")

#Example 5
def missingNumber(size, data):
    total=size*(size+1)//2
    actual=sum(data)
    return total-actual
print("Enter the range of elements")
size=int(input())
print("Enter the value of elements in an array")
data=[int(input()) for _ in range(size-1)]
missing=missingNumber(size, data)
print(f"The missing element is {missing}")

#Example 6
def detect_spikes(signal):
    spikes = []
    n = len(signal)
    i = 0
    while i < n - 1:
        while i < n - 1 and signal[i] == signal[i + 1]:
            i += 1
        start = i
        if i < n - 1:
            direction = 1 if signal[i] < signal[i + 1] else -1
            while i < n - 1 and (signal[i + 1] - signal[i]) * direction > 0:
                i += 1
            peak = i
            direction *= -1
            while i < n - 1 and (signal[i + 1] - signal[i]) * direction > 0:
                i += 1
            end = i
            if signal[end] == signal[start] and end > start + 1:
                origin = start + 1  
                span = end - start + 1
                spikes.append((origin, span))
        i = start + 1
    return spikes
import sys
data = list(map(int, sys.stdin.read().split()))
n = data[0]
signal = data[1:n+1]
spikes = detect_spikes(signal)
print(len(spikes))
for origin, span in spikes:
    print(origin,span)