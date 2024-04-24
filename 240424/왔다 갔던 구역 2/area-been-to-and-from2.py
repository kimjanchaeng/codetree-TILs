n=int(input())

block=[0]*200
c=100
for i in range(n):
    a, b= list(map(str,input().split()))
    
    if b=='R':
        for j in range(c,c+int(a)):
            block[j]+=1
            c=j
    else:
        for j in range(c-int(a),c):
            block[j]+=1
            c=j
count=0
for i in block:
    if i>1:
        count+=1

print(count)