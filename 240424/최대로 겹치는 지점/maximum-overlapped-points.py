n=int(input())

block=[0]*101
for i in range(n):
    a, b = list(map(int,input().split()))
    for j in range(a,b):
        block[j]+=1

count=0
for i in block:
    if i>1:
        count+=1

print(count)