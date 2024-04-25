n=int(input())
rows = 200
cols = 200

block = [[0 for j in range(cols)] for i in range(rows)]


for i in range(n):
    x1, y1, x2, y2=list(map(int,input().split()))
    x1+=100
    y1+=100
    x2+=100
    y2+=100
    for i in range(x1,x2):
        for j in range(y1,y2):
            block[i][j]+=1

count=0
for i in block:
    for j in i:
        if j>0:
            count+=1
print(count)