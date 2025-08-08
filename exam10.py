# Problem 1
class base:
    def __init__(self,n,m):
        self.n=n
        self.m=m
class sub(base):
    def sub_class(self):
        print(self.n,self.m)
n=int(input())
m=int(input())
obj=sub(n,m)
obj.sub_class()

# Problem 2
class base:
    def __init__(self):
        self._text=""
    def set_text(self,text):
        self._text=text
    def get_text(self):
        return self._text
msg=base()
input_text=input()
msg.set_text(input_text)
print(msg.get_text())

# Problem 3
a,b=map(int,input().split())
gcd=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
lcm=(a*b)//gcd
print(lcm)

# Problem 4
n=int(input())
m=input()
d={}
for i in m:
    if i in d:
        d[i]+=1
    else:
        d[i]+=1
print("Character Occurrences:")
for k,v in d.items():
    print(f"{k} : {v}")

# Problem 5
n=int(input())
a=[list(map(int,input().splpit())) for _ in range(n)]
b=[list(map(int,input().split())) for _ in range(m)]
for i in range(n):
    row=[]
    for j in range(n):
        s=0
        for k in range(n):
            s+=a[i][k]*b[k][j]
        row.append(s)
    print(*row)
