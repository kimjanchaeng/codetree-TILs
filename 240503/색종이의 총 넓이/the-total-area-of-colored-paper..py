n=int(input())

row=210

block=[[0 for i in range(row)] for j in range(row)]
# block=[[0]*row for i in range(row)]

for i in range(n):
    x,y=list(map(int,input().split()))
    x+=100
    y+=100

    for i in range(x,x+8):
        for j in range(y,y+8):
            block[i][j]+=1

count=0
for i in range(row):
    for j in range(row):
        if block[i][j]>0:
            count+=1
print(count)