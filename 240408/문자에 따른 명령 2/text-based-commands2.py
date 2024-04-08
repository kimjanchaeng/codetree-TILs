# dir=list(map(str,input().split()))
dir=list(input())
x,y=0,0
dx, dy= [1,0,-1,0],[0,-1,0,1]
dir_n=3

for i in dir:
    if i=='L':
        dir_n=(dir_n+3)%4
    elif i=='R':
        dir_n=(dir_n+1)%4
    else:
        x+=dx[dir_n]
        y+=dy[dir_n]

print(x,y)