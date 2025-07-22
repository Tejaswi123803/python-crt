#Extract unique digits from tuple list
n=int(input())
digits=set()
for _ in range(n):
    a,b=input().split()
    digits.update(a)
    digits.update(b)
unique_digits=sorted(set(filter(str.isdigit,digits)))
print("The extracted digits:", ' '.join(unique_digits))