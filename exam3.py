#Frequency count
n=input()
freq_map={}
for char in n:
    if char not in freq_map:
        freq_map[char]=1
    else:
        freq_map[char]+=1
output=", ".join([f"{char}={freq_map[char]}" for char in freq_map])
print("{"+output+"}")

#Modules mapping
n=int(input())
numbers=list(map(int,input().split()))
mod_map={}
for num in numbers:
    mod_map[num]=num%3
output=", ".join(f"{k}={v}" for k,v in mod_map.items())
print("{"+output+"}")

#Even length words
n=int(input())
words=input().split()
even_length_dict={word:len(word) for word in words if len(word)%2==0}
output=", ".join([f"{k}={v}" for k,v in even_length_dict.items()])
print("{"+output+"}")

#Upper case mapping
n=int(input())
word_map={}
for _ in range(n):
    word=input().strip()
    word_map[word]=word.upper()
output=", ".join([f"{key}={value}" for key,value in word_map.items()])
print("{"+output+"}")

#Squares dictionary
n=int(input())
result={}
for i in range(1,n+1):
    result[i]=i*i
output=", ".join(f"{k}={v}" for k,v in result.items())
print("{"+output+"}")