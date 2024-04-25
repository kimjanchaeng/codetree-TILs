row=2000
offset=1000
block=[[0]*row for i in range(row)]


for i in range(3):
    x1, y1, x2, y2 = list(map(int,input().split()))
    x1+=offset
    x2+=offset
    y1+=offset
    y2+=offset
    if i!=2:
        for j in range(x1,x2):
            for k in range(y1,y2):
                block[j][k]+=1
    else:
        for j in range(x1,x2):
            for k in range(y1,y2):
                block[j][k]-=1

count=0
for i in block:
    for j in i:
        if j==1:
            count+=1
print(count)