n=int(input())
max_r=200
offset=100

block=[['w']*max_r for i in range(max_r)]

for i in range(n):
    x1, y1, x2, y2=list(map(int,input().split()))
    x1+=offset
    y1+=offset
    x2+=offset
    y2+=offset

    if i%2==0:
        for i in range(x1,x2):
            for j in range(y1,y2):
                block[i][j]='r'
    else:
        for i in range(x1,x2):
            for j in range(y1,y2):
                block[i][j]='b'

area=0
for i in range(max_r):
    for j in range(max_r):
        if block[i][j]=='b':
            area+=1

print(area)